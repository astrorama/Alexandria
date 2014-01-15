#! /usr/bin/env python

import os
import subprocess

def executeThread(startLine, sourceNumber, outFile):
    print 'Starting new ProtoZpdf process with configuration:'
    print 'Lines: ['+str(startLine)+','+str(startLine+sourceNumber-1)+']'
    print 'Output file:', outFile
    logFile = outFile + '.log'
    print 'Log file:', logFile,'\n'
    command = []
    command.append('ProtoZpdf')
    command.append('--log-file='+logFile)
    command.append('--catalog-start-line='+str(startLine))
    command.append('--source-number='+str(sourceNumber))
    command.append('--catalog-output-file='+outFile)
    DEVNULL = open(os.devnull, 'wb')
    return subprocess.Popen(command, stdout=DEVNULL, stderr=DEVNULL)

def runInParallel(startLine, sourceNumber, threadNo, outFile):
    stepNumber = int(sourceNumber / threadNo)
    startLineList = []
    sourceNumberList = []
    outFileList = []
    for i in range(threadNo):
        startLineList.append(startLine)
        startLine += stepNumber
        sourceNumberList.append(stepNumber)
        outFileList.append(outFile + '.' + str(i))
    for i in range(sourceNumber % threadNo):
        sourceNumberList[i] = sourceNumberList[i] + 1
        for j in range(i+1, threadNo):
            startLineList[j] = startLineList[j] + 1
    threadList = []
    for i in range(threadNo):
        threadList.append(executeThread(startLineList[i], sourceNumberList[i], outFileList[i]))
    for i in range(threadNo):
        threadList[i].wait()
    print 'Merging catalogs...'
    with open(outFile,'w') as fullCatalog:
        for partCatalog in outFileList:
            print partCatalog
            with open(partCatalog) as partFile:
                for line in partFile.readlines():
                    fullCatalog.write(line)

def parseConfFile(confFile):
    startLine = -1
    sourceNumber = -1
    outFile = ''
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
                outFile = value.strip()
    if startLine == -1:
        print 'Configuration file does not define the catalog-start-line'
        exit()
    if sourceNumber == -1:
        print 'Configuration file does not define the source-number'
        exit()
    if not outFile:
        print 'Configuration file does not define the catalog-output-file'
        exit()
    return (startLine,sourceNumber, outFile)

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
    
    startLine, sourceNumber, outFile = parseConfFile(confFile)

    threadNo = args.threadno
    if not threadNo:
        import multiprocessing
        threadNo = multiprocessing.cpu_count()
    if threadNo <= 0:
        print 'Thread number must be positive but was', threadNo
        exit()
    if threadNo > sourceNumber:
        threadNo = sourceNumber
    
    runInParallel(startLine, sourceNumber, threadNo, outFile)
