#! /usr/bin/env python

import os
import subprocess
from astropy.io import fits

def executeThread(startLine, sourceNumber, outCatalogFile, outPdfFile):
    print 'Starting new ProtoZpdf process with configuration:'
    print 'Lines: ['+str(startLine)+','+str(startLine+sourceNumber-1)+']'
    print 'Output catalog file:', outCatalogFile
    print 'Output pdf file:', outPdfFile
    logFile = outCatalogFile + '.log'
    print 'Log file:', logFile,'\n'
    command = []
    command.append('ProtoZpdf')
    command.append('--log-file='+logFile)
    command.append('--catalog-start-line='+str(startLine))
    command.append('--source-number='+str(sourceNumber))
    command.append('--catalog-output-file='+outCatalogFile)
    command.append('--pdf-data-output-file='+outPdfFile)
    DEVNULL = open(os.devnull, 'wb')
    return subprocess.Popen(command, stdout=DEVNULL, stderr=DEVNULL)


def runInParallel(startLine, sourceNumber, threadNo, outCatalogFile, outPdfFile):
    stepNumber = int(sourceNumber / threadNo)
    startLineList = []
    sourceNumberList = []
    outCatalogFileList = []
    outPdfFileList = []
    for i in range(threadNo):
        startLineList.append(startLine)
        startLine += stepNumber
        sourceNumberList.append(stepNumber)
        outCatalogFileList.append(outCatalogFile + '.' + str(i))
        outPdfFileList.append(outPdfFile + '.' + str(i))
    for i in range(sourceNumber % threadNo):
        sourceNumberList[i] = sourceNumberList[i] + 1
        for j in range(i+1, threadNo):
            startLineList[j] = startLineList[j] + 1
    threadList = []
    for i in range(threadNo):
        threadList.append(executeThread(startLineList[i], sourceNumberList[i], outCatalogFileList[i], outPdfFileList[i]))
    for i in range(threadNo):
        threadList[i].wait()
    print 'Merging catalogs...'
    with open(outCatalogFile,'w') as fullCatalog:
        for partCatalog in outCatalogFileList:
            print partCatalog
            with open(partCatalog) as partFile:
                for line in partFile.readlines():
                    fullCatalog.write(line)
    print '\nMerging pdf FITS files...'
    hduList = []
    hduList.append(fits.PrimaryHDU())
    for partPdf in outPdfFileList:
        print partPdf
        for hdu in fits.open(partPdf):
            if type(hdu) is fits.hdu.BinTableHDU:
                hduList.append(hdu)
    if os.path.isfile(outPdfFile):
        os.remove(outPdfFile)
    fits.HDUList(hduList).writeto(outPdfFile)


def parseConfFile(confFile):
    startLine = -1
    sourceNumber = -1
    outCatalogFile = ''
    outPdfFile = ''
    with open(confFile) as f:
        for line in f.readlines():
            line = line.strip()
            if line.startswith('#') or not '=' in line:
                continue
            key,value = line.split('=', 1)
            if (key.strip() == 'catalog-start-line'):
                startLine = int(value.strip())
            if (key.strip() == 'source-number'):
                sourceNumber = int(value.strip())
            if (key.strip() == 'catalog-output-file'):
                outCatalogFile = value.strip()
            if (key.strip() == 'pdf-data-output-file'):
                outPdfFile = value.strip()
    if startLine == -1:
        print 'Configuration file does not define the catalog-start-line'
        exit()
    if sourceNumber == -1:
        print 'Configuration file does not define the source-number'
        exit()
    if not outCatalogFile:
        print 'Configuration file does not define the catalog-output-file'
        exit()
    if not outPdfFile:
        print 'Configuration file does not define the pdf-data-output-file'
        exit()
    return (startLine,sourceNumber, outCatalogFile, outPdfFile)


if __name__ == '__main__':

    from argparse import ArgumentParser
    parser = ArgumentParser(description='Executes the ProtoZpdf in parallel.')
    parser.add_argument("-c", "--conf", help="ProtoZ configuration file", metavar='FILE')
    parser.add_argument("-t", "--threadno", help="Number of threads to use", metavar='NUMBER', type=int)
    args = parser.parse_args()

    confFile = args.conf
    if not confFile:
        for confPath in os.environ.get('ELEMENTS_CONF_PATH').split(':'):
            if os.path.isfile(confPath + '/ProtoZ/ProtoZpdf.conf'):
                confFile = confPath + '/ProtoZ/ProtoZpdf.conf'
                break
    if not os.path.isfile(confFile):
        print 'Cannot find config file. Try specifying it with the -c option.'
        exit()
    
    startLine, sourceNumber, outCatalogFile, outPdfFile = parseConfFile(confFile)

    threadNo = args.threadno
    if not threadNo:
        import multiprocessing
        threadNo = multiprocessing.cpu_count()
    if threadNo <= 0:
        print 'Thread number must be positive but was', threadNo
        exit()
    if threadNo > sourceNumber:
        threadNo = sourceNumber
    
    runInParallel(startLine, sourceNumber, threadNo, outCatalogFile, outPdfFile)
