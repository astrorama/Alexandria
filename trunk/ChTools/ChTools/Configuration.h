/*
 * Configuration.h
 *
 *  Created on: Feb 27, 2013
 *      Author: Thomas Bretz
 */

#ifndef CONFIGURATION_H_
#define CONFIGURATION_H_

#include <iostream>
#include <functional>
#include <map>
#include <boost/program_options.hpp>

namespace po = boost::program_options;

class Configuration {
private:
  /// Convenience enum to access the fOption* data members more verbosely.
  enum {
    kHidden = 0, ///< Index for hidden options (not shown in printParsed)
    kVisible = 1  ///< Index for options visible in printParsed
  };

  const std::string fName; /// argv[0]

  std::map<std::string, std::string> fEnvMap;

  po::options_description fOptionsCommandline[2]; /// Description of the command-line options
  po::options_description fOptionsConfigfile[2]; /// Description of the options in the configuration file
  po::options_description fOptionsDatabase[2]; /// Description of options from the database
  po::options_description fOptionsEnvironment[2]; /// Description of options from the environment

  po::positional_options_description fArgumentPositions; /// Description of positional command-line options (arguments)

  std::vector<std::string> fUnknownCommandline; /// Storage container for unrecognized commandline options
  std::vector<std::string> fUnknownConfigfile; /// Storage container for unrecognized options from configuration files
  std::vector<std::string> fUnknownEnvironment; /// Storage container for unrecognized options from the environment
  std::vector<std::string> fUnknownDatabase; /// Storage container for unrecognized options retrieved from the database

  std::map<std::string, std::string> fWildcardOptions; /// Options which were registered using wildcards

  std::string fPriorityFile; /// File name of the priority configuration file (overwrites option from the databse)
  std::string fDefaultFile; /// File name of the default configuration file (usually {program}.rc)
  std::string fDatabase; /// URL for database connection (see Configuration::parseDatabase)

  po::variables_map fVariables; /// Variables as compiled by the parse-function, which will be passed to the program

  /// A default mapper for environment variables skipping all of them
  std::string DefaultMapper(const std::string env) {
    return fEnvMap[env];
  }

  /// Pointer to the mapper function for environment variables
  std::function<std::string(std::string)> fNameMapper;
  std::function<void()> fPrintUsage;
  std::function<void(const std::string&)> fPrintVersion;

  /// Helper function which return the max of the two arguments in the first argument
  static void Max(int &val, const int &comp) {
    if (comp > val)
      val = comp;
  }

  /// Helper for parse to create list of used wildcard options
  void createWildcardOptions();

  // Helper functions for printOptions and getOptions
  template<class T>
  std::string vecAsStr(const po::variable_value &v) const;
  std::string varAsStr(const po::variable_value &v) const;

  /// Print all options from a list of already parsed options
  void printParsed(const po::parsed_options &parsed) const;
  /// Print a list of all unkown options within the given vector
  void printUnknown(const std::vector<std::string> &vec, int steps = 1) const;

  virtual void PrintUsage() const {
  }
  virtual void printVersion() const;

  std::string unLibToolize(const std::string &src) const;

public:
  Configuration(const std::string &prgname = "");
  virtual ~Configuration() {
  }

  /// Retrieve data from a database and return them as options
  static po::basic_parsed_options<char>
  parseDatabase(const std::string &prgname, const std::string &database,
      const po::options_description& desc, bool allow_unregistered = false);

  // Setup
  void addOptionsCommandline(const po::options_description &cl, bool visible =
      true);
  void addOptionsConfigFile(const po::options_description &cf, bool visible =
      true);
  void addOptionsEnvironment(const po::options_description &env, bool visible =
      true);
  void addOptionsDatabase(const po::options_description &db,
      bool visible = true);
  void addOptions(const po::options_description &opt, bool visible = true) {
    addOptionsCommandline(opt, visible);
    addOptionsConfigFile(opt, visible);
    addOptionsEnvironment(opt, visible);
    addOptionsDatabase(opt, visible);
  }

  void setArgumentPositions(const po::positional_options_description &desc);

  void setNameMapper(const std::function<std::string(std::string)> &func);
  void setNameMapper();

  void setPrintUsage(const std::function<void(void)> &func);
  void setPrintUsage();

  void setPrintVersion(const std::function<void(const std::string &)> &func);
  void setPrintVersion();

  void addEnv(const std::string &conf, const std::string &env) {
    fEnvMap[env] = conf;
  }

  // Output
  void printOptions() const;
  void printUnknown() const;
  void printWildcardOptions() const;

  const std::map<std::string, std::string> &getWildcardOptions() const {
    return fWildcardOptions;
  }
  const std::vector<std::string> getWildcardOptions(
      const std::string &opt) const;

  template<class T>
  const std::map<std::string, T> getOptions(const std::string &opt) {
    const std::vector<std::string> rc = getWildcardOptions(opt + '*');

    std::map<std::string, T> map;
    for (auto it = rc.begin(); it != rc.end(); it++)
      map[it->substr(opt.length())] = get<T>(*it);

    return map;
  }

  std::multimap<std::string, std::string> getOptions() const;

  // Process command line arguments
  const po::variables_map &parse(int argc, const char **argv,
      const std::function<void()> &func = std::function<void()>());
  bool doParse(int argc, const char **argv, const std::function<void()> &func =
      std::function<void()>());

  bool hasVersion() {
    return has("version");
  }

  bool hasHelp() {
    return has("help") || has("help-config") || has("help-env")
        || has("help-database");
  }

  bool hasPrint() {
    return has("print-all") || has("print") || has("print-default")
        || has("print-database") || has("print-config")
        || has("print-environment") || has("print-unknown")
        || has("print-options") || has("print-wildcards");
  }

  // Simplified access to the parsed options
  template<class T>
  T get(const std::string &var) {
    fWildcardOptions.erase(var);
    return fVariables[var].as<T>();
  }
  bool has(const std::string &var) {
    fWildcardOptions.erase(var);
    return fVariables.count(var) > 0;
  }

  template<class T>
  std::vector<T> vec(const std::string &var) {
    return has(var) ? fVariables[var].as<std::vector<T>>() : std::vector<T>();
  }

  template<class T, class S>
  T get(const std::string &var, const S &val) {
    std::ostringstream str;
    str << var << val;
    return get<T>(str.str());
  }

  template<class T>
  bool has(const std::string &var, const T &val) {
    std::ostringstream str;
    str << var << val;
    return has(str.str());
  }

  template<class T, class S>
  T getDef(const std::string &var, const S &val) {
    return has(var, val) ? get<T>(var, val) : get<T>(var + "default");
  }

  template<class T>
  bool hasDef(const std::string &var, const T &val) {
    // Make sure the .default option is touched
    const bool rc = has(var + "default");

    return has(var, val) ? true : rc;
  }

  void remove(const std::string &var) {
    fVariables.erase(var);
  }

  /*
   template<class T>
   std::map<std::string, T> getMap(const std::string &var)
   {
   const size_t len = var.length();

   std::map<std::string, T> rc;
   for (std::map<std::string, boost::program_options::variable_value>::const_iterator it=fVariables.begin();
   it!=fVariables.end(); it++)
   if (it->first.substr(0, len)==var)
   rc[it->first] = it->second.as<T>();

   return rc;
   }

   template<class T>
   std::vector<std::string> getKeys(const std::string &var)
   {
   const size_t len = var.length();

   std::vector<std::string> rc;
   for (std::map<std::string, boost::program_options::variable_value>::const_iterator it=fVariables.begin();
   it!=fVariables.end(); it++)
   if (it->first.substr(0, len)==var)
   rc.push_back(it->first);

   return rc;
   }
   */
  const std::string &getName() const {
    return fName;
  }
};

template<typename T>
struct Hex {
  T val;
  Hex() {
  }
  Hex(const T &v) :
      val(v) {
  }
  operator T() const {
    return val;
  }
};
template<typename T>
std::istream &operator>>(std::istream &in, Hex<T> &rc) {
  T val;
  in >> std::hex >> val;
  rc.val = val;
  return in;
}

template<class T>
inline po::typed_value<T> *var(T *ptr = 0) {
  return po::value<T>(ptr);
}

template<class T>
inline po::typed_value<T> *var(const T &val, T *ptr = 0) {
  return po::value<T>(ptr)->default_value(val);
}

template<class T>
inline po::typed_value<std::vector<T>> *vars() {
  return po::value<std::vector<T>>();
}

inline po::typed_value<bool> *po_switch() {
  return po::bool_switch();
}

inline po::typed_value<bool> *po_bool(bool def = false) {
  return po::value<bool>()->implicit_value(true)->default_value(def);
}

#endif /* CONFIGURATION_H_ */
