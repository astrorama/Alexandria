/**
 * @file Configuration.cpp
 * @date Feb 27, 2013
 * @author Thomas Bretz
 */

// **************************************************************************
/** @class Configuration

 @brief Commandline parsing, resource file parsing and database access


 @section User For the user

 The Configuration class will process the following steps:

 Check the command-line for <B> --default=default.rc </B> (If no configuration
 filename is given on the command-line use \e program_name.rc instead. (Note
 that the name is retrieved from \b argv[0] and might change if you start
 the program through a symbolic link with a different name)

 Read the "<B>database=user:password@database:port/database</B>" entry from the file.
 (For details about the syntax see Configuration::parseDatabase)
 The retrieved entry can be overwritten by
 "<B>--database=user:passwd@server:port/database</B>" from the command line. If
 neither option is given no configuration data will be read from the
 database. To suppress any database access use \b --no-database.

 Check the command-line for <B> -C priority.rc </B>

 The configuration data is now evaluated from the following sources in
 the following order. Note that options from earlier source have
 priority.

 - (1) Commandline options
 - (2) Options from the high prioroty configuration-file (given by \b -C or \b --config)
 - (3) Database entries
 - (4) Options from the default configuration-file (given by \b --default, defaults to \b program_name.rc)
 - (5) Options from the global configuration-file (constructor path + \b fact++.rc)
 - (6) Environment variables

 Which options are accepted is defined by the program. To get a list
 of all command-line option use \b --help. This also lists all other
 available options to list for example the options available in the
 configuration files or from the database. In addition some default options
 are available which allow to debug parsing of the options, by either printing
 the options retrieval or after parsing.

 Options in the configuration files must be given in the form

 - key = value

 which is equivalent to the command-line option <B>--key=value</B>.

 If there are sections in the configuration file like

 \code

 [section1]
 key = value

 \endcode

 the key is transformed into <B>section1.key</B> (which would be equivalent
 to <B>--section1.key</B>)

 @attention
 In principle it is possible that an exception is thrown before options
 like \b --help are properly parsed and evaluated. In this case it is
 necessary to first resolve the problem. Usually, this mean that there
 is a design flaw in the program rather than a mistake of usage.

 For more details on the order in which configuration is read,
 check Configuration::parse. For more details on the parsing itself
 see the documentation of boost::program_options.




 @section API For the programmer

 The Configuration class heavily uses the
 <A HREF="http://www.boost.org"><B>C++ boost library</B></A>
 and makes heavy use of the
 <A HREF="http://www.boost.org/doc/libs/release/doc/html/program_options.html">
 <B>boost::program_options</B></A>

 The databse access is based on the
 <A HREF="http://tangentsoft.net/mysql++/"><B>MySQL++ library</B></A>.

 The basic idea is to have an easy to use, but powerfull setup. The setup on
 all options is based on a special syntax of options_description. Here is an
 example:

 \code

 int opt = 0;

 po::options_description config("Section");
 config.add_options()
 ("option1",    var<string>(),                        "This is option1")
 ("option2",    var<int>(22),                         "This is option2")
 ("option3,o",  var<double>->required(),              "This option is mandatory")
 ("option4",    var<int>(&opt),                       "This is option 4")
 ("option5",    vars<string>(),                       "A list of strings")
 ("option6",    vars<string>(),                       "A list of strings")
 ("option7",    vars<string>,                         "A list of strings")
 ("option8",    var<string>()->implicit_value("val"), "Just a string")
 ("option9",    var<string>()->default_value("def"),  "Just a string")
 ("optionA",    var<string>("def"),                   "Just a string")
 ("bool",       po_bool(),                            "A special switch")
 ;

 \endcode

 This will setup, e.g.,  the commandline option '<B>--option1 arg</B>' (which
 is identical to '<B>--option1=arg</B>'. Option 3 can also be expressed
 in a short form as '<B>-o arg</B>' or '<B>-o=arg</B>'. Option 2 defaults
 to 22 if no explicit value is given. Option 3 is mandatory and an exception
 is thrown if not specified. Option 4 will, apart from the usual access to the
 option values, also store its value in the variable opt.

 The used functions po_*() are defined in configuration.h and are abbreviations.
 Generally speaking also other variable types are possible.

 If the options are displayed, e.g. by \b --help the corresponding section will
 by titled \e Section, also untitled sections are possible.

 If an option can be given more than once then a std::vector<type> can be used.
 Abbreviations po_ints(), po_doubles() and po_strings() are available.

 There are several ways to define the behaviour of the options. In the
 example above parse will throw an exception if the "--option3" or "-o"
 option is not given. "option9" will evaluate to "def" if it is not
 given on the command line. The syntax of "optionA" is just an
 abbreviation. "option8" will evaluate to "val" if just "--option5" but
 no argument is given. Note, that these modifiers can be concatenated.

 A special type po_bool() is provided which is an abbreviation of
 var<bool>()->implicit_value(true)->default_value(false). In
 contradiction to po_switch() this allows to set a true and
 false value in the setup file.

 In addition to options introduced by a minus or double minus, so called
 positional options can be given on the command line. To describe these
 options use

 \code

 po::positional_options_description p;
 p.add("option5", 2); // The first 2 positional options
 p.add("option6", 3); // The next three positional options
 // p.add("option7", -1); // All others, if wanted

 \endcode

 This assigns option-keys to the positional options (arguments) in the
 command-line. Note that the validity of the given commandline is checked.
 Hence, this way of defining the options makes sense.

 As needed options_descriptions can be grouped together

 \code

 po::options_description config1("Section1");
 po::options_description config2("Section2");

 po::options_description configall;
 configall.add(config1);
 configall.add(config2);

 \endcode

 The member functions of Configurations allow to define for which option
 source these options are valid. The member functions are:

 \code

 Configuration conf;

 conf.addOptionsCommandline(configall, true);
 conf.addOptionsConfigFile(config1, true);
 conf.addOptionsDatabase(config2, true);

 // To enable the mapping of the position arguments call this
 conf.setArgumentPositions(p);

 \endcode

 If the second option is false, the options will not be displayed in any
 \b --help directive, but are available to the user. Each of the functions
 can be called more than once. If an option should be available from
 all kind of inputs addOptions() can be used which will call all
 four other addOptions() functions.

 A special case are the options from environment variables. Since you might
 want to use the same option-key for the command-line and the environment,
 a mapping is needed (e.g. from \b PATH to \b --path). This mapping
 can be implemented by a mapping function or by the build in mapping
 and be initialized like this:

 \code

 conf.addEnv("path", "PATH");

 \endcode

 or

 \code

 const string name_mapper(const string str)
 {
 return str=="PATH" ? "path" : "";
 }

 conf.setNameMapper(name_mapper);

 \endcode

 Assuming all the above is done in a function calls SetupConfiguration(),
 a simple program to demonstrate the power of the class could look like this:

 \code

 int main(int argc, char **argv)
 {
 int opt;

 Configuration conf(argv[0]);
 SetupConfiguration(conf, opt);

 po::variables_map vm;
 try
 {
 vm = conf.parse(argc, argv);
 }
 catch (std::exception &e)
 {
 po::multiple_occurrences *MO = dynamic_cast<po::multiple_occurrences*>(&e);
 if (MO)
 cout << "Error: " << e.what() << " of '" << MO->get_option_name() << "' option." << endl;
 else
 cout << "Error: " << e.what() << endl;
 cout << endl;

 return -1;
 }

 cout << "Opt1: " << conf.GetString("option1") << endl;
 cout << "Opt2: " << conf.GetInt("option2") << endl;
 cout << "Opt3: " << conf.GetDouble("option3") << endl;
 cout << "Opt4: " << opt << endl;

 return 0;
 }

 \endcode

 Another possibility to access the result is the direct approach, for example:

 \code

 vector<int>    i   = vm["option2"].as<int>();
 vector<string> vec = vm["option6"].as<vector<string>>();

 \endcode

 Note that accessing an option which was not given will throw an exception.
 Therefore its availability should first be checked in one of the following
 ways:

 \code

 bool has_option1 = vm.count("option1");
 bool has_option2 = conf.has("option2");

 \endcode

 @section Extensions

 The configuration interpreter can be easily extended to new types, for example:

 \code

 template<class T,class S> // Just for the output
 std::ostream &operator<<(std::ostream &out, const pair<T,S> &f)
 {
 out << f.first << "|" << f.second;
 return out;
 }

 template<class T, class S> // Needed to convert the option
 std::istream &operator>>(std::istream &in,  pair<T,S> &f)
 {
 char c;
 in >> f.first;
 in >> c;
 if (c!=':')
 return in;
 in >> f.second;
 return in;
 }

 typedef pair<int,int> mytype; // Type definition

 void main(int argc, char **argv)
 {
 po::options_description config("Configuration");
 config.add_options()
 ("mytype", var<mytype>(), "my new type")
 ;

 Configuration conf;
 conf.addOptionsCommandline(config);
 conf.parse(argc, argv);

 cout << conf.Get<mytype>("mytype") << endl;
 }

 \endcode

 @todo:
 - Maybe we should remove the necessity to propagate argv[0] in the constructor?
 - Add an option to the constructor to switch of database/file access

 */
// **************************************************************************
#include "ChTools/Configuration.h"

#include <fstream>
#include <iostream>
#include <iomanip>
#include <string>

#include <boost/filesystem.hpp>

#ifdef HAVE_SQL
#include "Database.h"
#endif

using namespace std;

namespace style = boost::program_options::command_line_style;

// --------------------------------------------------------------------------
//
//!  The purpose of this function is basically to connect to the database,
//!  and retrieve all the options entries from the 'Configuration' table.
//!
//!  @param prgname
//!      Name of the program
//!
//!  @param database
//!      The URL of the database from which the configuration data is
//!      retrieved. It should be given in the form
//!          \li [user[:password]@]server.com[:port]/database
//!
//!      with
//!          - user:     user name (default is the current user)
//!          - password: necessary if required by the database rights
//!          - server:   the URL of the server (can be 'localhost')
//!          - port:     the port to which to connect (usually obsolete)
//!          - database: The name of the database containing the table
//!
//!  @param desc
//!     A reference to the object with the description of the options
//!     which should be retrieved.
//!
//!  @param allow_unregistered
//!     If this is true also unregistered, i.e. options unknown to desc,
//!     are returned. Otherwise an exception is thrown if such an option
//!     was retrieved.
//!
//!  @return
//!     Return an object of type basic_parsed_options containing all
//!     the entries retrieved from the database. Options not found in
//!     desc are flagged as unregistered.
//!
//!  @throws
//!     Two types of exceptions are thrown
//!        - It thows an unnamed exception if the options could not be
//!          retrieved properly from the databse.
//!        - If an option is not registered within the given descriptions
//!          and \b allow_unregistered is \b false, an exception of type
//!          \b  po::unknown_option is thrown.
//!
//!  @todo
//!     - The exceptions handling should be improved.
//!     - The final database layout is missing in the description
//!     - Shell we allow options to be given more than once?
//
#ifdef HAVE_SQL
po::basic_parsed_options<char>
Configuration::parseDatabase(const string &prgname, const string &database, const po::options_description& desc, bool allow_unregistered)
{
  Database db(database);

  cout << "Connected to '" << db.uri() << "' for " << prgname << endl;

  const mysqlpp::StoreQueryResult res =
  db.query("SELECT CONCAT(fKey1,fKey2), fValue "
      "FROM ProgramOption "
      "WHERE fCounter=(SELECT MAX(fCounter) FROM History) "
      "AND NOT ISNULL(fValue) "
      "AND (fProgram='"+prgname+"' OR fProgram='*')").store();

  set<string> allowed_options;

  const vector<boost::shared_ptr<po::option_description>> &options = desc.options();
  for (unsigned i=0; i<options.size(); ++i)
  {
    const po::option_description &d = *options[i];
    if (d.long_name().empty())
    boost::throw_exception(po::error("long name required for database"));

    allowed_options.insert(d.long_name());
  }

  po::parsed_options result(&desc);

  for (vector<mysqlpp::Row>::const_iterator v=res.begin(); v<res.end(); ++v)
  {
    const string key = (*v)[0].c_str();
    if (key.empty())  // key  == > Throw exception
    continue;

    // Check if we are allowed to accept unregistered options,
    // i.e. options which are not in options_description &desc.
    const bool unregistered = allowed_options.find(key)==allowed_options.end();
    if (unregistered && allow_unregistered)
    boost::throw_exception(po::unknown_option(key));

    // Create a key/value-pair and store whether it is a
    // registered option of not
    po::option n;
    n.string_key = key;
    // This is now identical to file parsing. What if we want
    // to concatenate options like on the command line?
    n.value.clear();// Fixme: composing?
    n.value.push_back((*v)[1].c_str());
    //n.unregistered = unregistered;

    // If any parsing will be done in the future...
    //n.value().original_tokens.clear();
    //n.value().original_tokens.push_back(name);
    //n.value().original_tokens.push_back(value);

    result.options.push_back(n);
  }

  return result;
}
#else
po::basic_parsed_options<char> Configuration::parseDatabase(const string &,
    const string &, const po::options_description &desc, bool) {
  return po::parsed_options(&desc);
}
#endif

// --------------------------------------------------------------------------
//
//!
//
Configuration::Configuration(const string &prgname) :
    fName(unLibToolize(prgname)), fNameMapper(
        bind1st(mem_fun(&Configuration::DefaultMapper), this)), fPrintUsage(
        bind(&Configuration::PrintUsage, this)) {
  po::options_description generic("Generic options");
  generic.add_options()("version,V", "Print version information.")("help",
      "Print available commandline options.")("help-environment",
      "Print available environment variables.")("help-database",
      "Print available options retreived from the database.")("help-config",
      "Print available configuration file options.")("print-all",
      "Print all options as parsed from all the different sources.")("print",
      "Print options as parsed from the commandline.")("print-default",
      "Print options as parsed from default configuration file.")(
      "print-database", "Print options as retrieved from the database.")(
      "print-config",
      "Print options as parsed from the high priority configuration file.")(
      "print-environment", "Print options as parsed from the environment.")(
      "print-unknown", "Print unrecognized options.")("print-options",
      "Print options as passed to program.")("print-wildcards",
      "Print all options registered with wildcards.")("dont-check",
      "Do not check validity of options from files and database.")(
      "dont-check-files", "Do not check validity of options from files.")(
      "dont-check-database", "Do not check validity of options from database.");

  po::options_description def_config;
  def_config.add_options()("default", var<string>(fName + string(".rc")),
      "Default configuration file.");

  po::options_description config("Configuration options");
  config.add_options()("config,C", var<string>(),
      "Configuration file overwriting options retrieved from the database.")(
      "database", var<string>(),
      "Database link as in\n\t[user[:password]@]server.com[:port]/database\nOverwrites options from the default configuration file.")(
      "no-database",
      "Suppress any access to the database even if a database URL was set.");

  fOptionsCommandline[kVisible].add(generic);
  fOptionsCommandline[kVisible].add(config);
  fOptionsCommandline[kVisible].add(def_config);
  fOptionsConfigfile[kVisible].add(config);
}

// --------------------------------------------------------------------------
//
//
void Configuration::printParsed(const po::parsed_options &parsed) const {
  const vector<po::basic_option<char> >& options = parsed.options;

  // .description -> Pointer to opt_commandline
  // const std::vector< shared_ptr<option_description> >& options() const;

  //const std::string& key(const std::string& option) const;
  //const std::string& long_name() const;
  //const std::string& description() const;
  //shared_ptr<const value_semantic> semantic() const;

  int maxlen = 0;
  for (unsigned i = 0; i < options.size(); ++i) {
    const po::basic_option<char> &opt = options[i];

    if (opt.value.size() > 0 && opt.string_key[0] != '-')
      Max(maxlen, opt.string_key.length());
  }

  cout.setf(ios_base::left);

  // =============> Implement prining of parsed options
  for (unsigned i = 0; i < options.size(); ++i) {
    const po::basic_option<char> &opt = options[i];

    if ( (opt.value.size() == 0) && (!opt.string_key[0] == '-') )
      cout << "--";
    cout << setw(maxlen) << opt.string_key;
    if (opt.value.size() > 0)
      cout << " = " << opt.value[0];

    //for (int j=0; j<options[i].value.size(); j++)
    //    cout << "\t = " << options[i].value[j];
    //cout << "/" << options[i].original_tokens[0];

    ostringstream com;

    if (opt.position_key >= 0)
      com << " [position=" << opt.position_key << "]";
    if (opt.unregistered)
      com << " [unregistered]";

    if (!com.str().empty())
      cout << "  # " << com.str();

    cout << endl;
  }
}

template<class T>
string Configuration::vecAsStr(const po::variable_value &v) const {
  ostringstream str;

  const vector<T> vec = v.as<vector<T>>();
  for (typename std::vector<T>::const_iterator s = vec.begin(); s < vec.end(); ++s)
    str << " " << *s;

  return str.str().substr(1);
}

string Configuration::varAsStr(const po::variable_value &v) const {
  if (v.value().type() == typeid(bool))
    return v.as<bool>() ? "yes " : "no";

  if (v.value().type() == typeid(string))
    return v.as<string>();

  if (v.value().type() == typeid(int16_t))
    return to_string((long long int) v.as<int16_t>());

  if (v.value().type() == typeid(int32_t))
    return to_string((long long int) v.as<int32_t>());

  if (v.value().type() == typeid(int64_t))
    return to_string((long long int) v.as<int64_t>());

  if (v.value().type() == typeid(uint16_t))
    return to_string((long long unsigned int) v.as<uint16_t>());

  if (v.value().type() == typeid(uint32_t))
    return to_string((long long unsigned int) v.as<uint32_t>());

  if (v.value().type() == typeid(uint64_t))
    return to_string((long long unsigned int) v.as<uint64_t>());

  if (v.value().type() == typeid(float))
    return to_string((long double) v.as<float>());

  if (v.value().type() == typeid(double))
    return to_string((long double) v.as<double>());

  if (v.value().type() == typeid(vector<string> ))
    return vecAsStr<string>(v);

  if (v.value().type() == typeid(vector<int16_t> ))
    return vecAsStr<int16_t>(v);

  if (v.value().type() == typeid(vector<int32_t> ))
    return vecAsStr<int32_t>(v);

  if (v.value().type() == typeid(vector<int64_t> ))
    return vecAsStr<int64_t>(v);

  if (v.value().type() == typeid(vector<uint16_t> ))
    return vecAsStr<uint16_t>(v);

  if (v.value().type() == typeid(vector<uint32_t> ))
    return vecAsStr<uint32_t>(v);

  if (v.value().type() == typeid(vector<uint64_t> ))
    return vecAsStr<uint64_t>(v);

  if (v.value().type() == typeid(vector<float> ))
    return vecAsStr<float>(v);

  if (v.value().type() == typeid(vector<double> ))
    return vecAsStr<double>(v);

  ostringstream str;
  str << hex << setfill('0') << "0x";
  if (v.value().type() == typeid(Hex<uint16_t> ))
    str << setw(4) << v.as<Hex<uint16_t>>();

  if (v.value().type() == typeid(Hex<uint32_t> ))
    str << setw(8) << v.as<Hex<uint32_t>>();

  if (v.value().type() == typeid(Hex<uint64_t> ))
    str << setw(16) << v.as<Hex<uint64_t>>();

  return str.str();
}

// --------------------------------------------------------------------------
//
//
void Configuration::printOptions() const {
  cout << "Options propagated to program:" << endl;

  int maxlen = 0;
  for (map<string, po::variable_value>::const_iterator m = fVariables.begin();
      m != fVariables.end(); ++m)
    Max(maxlen, m->first.length());

  cout.setf(ios_base::left);

  // =============> Implement prining of options in use
  for (map<string, po::variable_value>::const_iterator m = fVariables.begin();
      m != fVariables.end(); ++m) {
    const po::variable_value &v = m->second;

    ostringstream str;

    if (v.value().type() == typeid(bool))
      str << " bool";
    if (v.value().type() == typeid(string))
      str << " string";
    if (v.value().type() == typeid(int16_t))
      str << " int16_t";
    if (v.value().type() == typeid(int32_t))
      str << " int32_t";
    if (v.value().type() == typeid(int64_t))
      str << " int64_t";
    if (v.value().type() == typeid(uint16_t))
      str << " uint16_t";
    if (v.value().type() == typeid(uint32_t))
      str << " uint32_t";
    if (v.value().type() == typeid(uint64_t))
      str << " uint64_t";
    if (v.value().type() == typeid(float))
      str << " float";
    if (v.value().type() == typeid(double))
      str << " double";
    if (v.value().type() == typeid(Hex<uint16_t> ))
      str << " Hex<uint16_t>";
    if (v.value().type() == typeid(Hex<uint32_t> ))
      str << " Hex<uint32_t>";
    if (v.value().type() == typeid(Hex<uint64_t> ))
      str << " Hex<uint64_t>";
    if (v.value().type() == typeid(vector<string> ))
      str << " vector<string>";
    if (v.value().type() == typeid(vector<int16_t> ))
      str << " vector<int16_t>";
    if (v.value().type() == typeid(vector<int32_t> ))
      str << " vector<int32_t>";
    if (v.value().type() == typeid(vector<int64_t> ))
      str << " vector<int64_t>";
    if (v.value().type() == typeid(vector<uint16_t> ))
      str << " vector<uint16_t>";
    if (v.value().type() == typeid(vector<uint32_t> ))
      str << " vector<uint32_t>";
    if (v.value().type() == typeid(vector<uint64_t> ))
      str << " vector<uint64_t>";
    if (v.value().type() == typeid(vector<float> ))
      str << " vector<float>";
    if (v.value().type() == typeid(vector<double> ))
      str << " vector<double>";

    if (str.str().empty())
      str << " unknown[" << v.value().type().name() << "]";

    const string var = varAsStr(v);
    cout << setw(maxlen) << m->first;
    if (!var.empty())
      cout << " = ";
    cout << var << "   #" << str.str();

    if (v.defaulted())
      cout << " [default]";
    if (v.empty())
      cout << " [empty]";

    cout << endl;
  }

  cout << endl;
}

// --------------------------------------------------------------------------
//
//
void Configuration::printUnknown(const vector<string> &vec, int steps) const {
  for (vector<string>::const_iterator v = vec.begin(); v < vec.end(); v +=
      steps)
    cout << " " << *v << endl;
  cout << endl;
}

multimap<string, string> Configuration::getOptions() const {
  multimap<string, string> rc;

  for (map<string, po::variable_value>::const_iterator m = fVariables.begin();
      m != fVariables.end(); ++m)
    rc.insert(pair<string, string>(m->first, varAsStr(m->second)));

  return rc;
}

// --------------------------------------------------------------------------
//
//
void Configuration::printUnknown() const {
  if (fUnknownCommandline.size()) {
    cout << "Unknown commandline options:" << endl;
    printUnknown(fUnknownCommandline);
  }

  if (fUnknownConfigfile.size()) {
    cout << "Unknown options in configfile:" << endl;
    printUnknown(fUnknownConfigfile, 2);
  }

  if (fUnknownEnvironment.size()) {
    cout << "Unknown environment variables:" << endl;
    printUnknown(fUnknownEnvironment);
  }

  if (fUnknownDatabase.size()) {
    cout << "Unknown database entry:" << endl;
    printUnknown(fUnknownDatabase);
  }
}

// --------------------------------------------------------------------------
//
//
void Configuration::addOptionsCommandline(const po::options_description &cl,
    bool visible) {
  fOptionsCommandline[visible].add(cl);
}

// --------------------------------------------------------------------------
//
//
void Configuration::addOptionsConfigFile(const po::options_description &cf,
    bool visible) {
  fOptionsConfigfile[visible].add(cf);
}

// --------------------------------------------------------------------------
//
//
void Configuration::addOptionsEnvironment(const po::options_description &env,
    bool visible) {
  fOptionsEnvironment[visible].add(env);
}

// --------------------------------------------------------------------------
//
//
void Configuration::addOptionsDatabase(const po::options_description &db,
    bool visible) {
  fOptionsDatabase[visible].add(db);
}

// --------------------------------------------------------------------------
//
//
void Configuration::setArgumentPositions(
    const po::positional_options_description &desc) {
  fArgumentPositions = desc;
}

// --------------------------------------------------------------------------
//
//
void Configuration::setNameMapper(const function<string(string)> &func) {
  fNameMapper = func;
}

void Configuration::setNameMapper() {
  fNameMapper = bind1st(mem_fun(&Configuration::DefaultMapper), this);
}

void Configuration::setPrintUsage(const function<void(void)> &func) {
  fPrintUsage = func;
}

void Configuration::setPrintUsage() {
  fPrintUsage = bind(&Configuration::PrintUsage, this);
}

void Configuration::setPrintVersion(const function<void(const string&)> &func) {
  fPrintVersion = func;
}

void Configuration::setPrintVersion() {
  fPrintVersion = function<void(const string&)>();
}

// --------------------------------------------------------------------------
//
//!
//! The idea of the parse() memeber-function is to parse the command-line,
//! the configuration files, the databse and the environment and return
//! a proper combined result.
//!
//! In details the following actions are performed in the given order:
//!
//!  - (0)  Init local variables with the list of options described by the
//!         data members.
//!  - (1)  Reset the data members fPriorityFile, fDefaultFile, fDatabase
//!  - (2)  parse the command line
//!  - (3)  Check for \b --help* command-line options and performe
//!         corresponding action
//!  - (4)  Check for \b --print and \b --print-all and perform corresponding
//!         action
//!  - (5)  Read and parse the global configuration file, which is compiled
//!         from the path corresponding to the argument given in the
//!         constructor + "/fact++.rc", unrecognized options are always
//!         allowed. Note that in contradiction to all other options
//!         the options in this file are not checked at all. Hence,
//!         typos might stay unnoticed.
//!  - (6)  Read and parse the default configuration file, which is either
//!         given by the default name or the \b --default command-line
//!         option. The default name is compiled from the argument
//!         given to the constructor and ".rc".  If the file-name is
//!         identical to the default (no command-line option given)
//!         a missing configuration file is no error. Depending on
//!         the \b --dont-check and \b --dont-check-files options,
//!         unrecognized options in the file throw an exception or not.
//!  - (7)  Check for \b --print-default and \b --print-all and perform
//!         corresponding action
//!  - (8)  Read and parse the priority configuration file, which must be given
//!         by the \b --config or \b -C command-line option or a
//!         corresponding entry in the default-configuration file.
//!         If an option on the command-line and the in the configuration
//!         file exists, the command-line option has priority.
//!         If none is given, no priority file is read. Depending on
//!         the \b --dont-check and \b --dont-check-files options,
//!         unrecognized options in the file throw an exception or not.
//!  - (9)  Check for \b --print-config and \b --print-all and perform
//!         corresponding action
//!  - (10) Retrieve options from the database according to the
//!         options \b --database and \b --no-database. Note that
//!         options given on the command-line have highest priority.
//!         The second priority is the priority-configuration file.
//!         The options from the default configuration-file have
//!         lowest priority.
//!  - (11) Check for \b --print-database and \b --print-all and perform
//!         corresponding action
//!  - (12) parse the environment options.
//!  - (13) Check for \b --print-environment and \b --print-all and perform
//!         corresponding action
//!  - (14) Compile the final result. The priority of the options is (in
//!         decreasing order): command-line options, options from the
//!         priority configuration file, options from the database,
//!         options from the default configuration-file and options
//!         from the environment.
//!  - (15) Find all options which were found and flagged as unrecognized,
//!         because they are not in the user-defined list of described
//!         options, are collected and stored in the corresponding
//!         data-members.
//!  - (16) Find all options which where registered with wildcards and
//!         store the list in fWildcardOptions.
//!  - (17) Before the function returns it check for \b --print-options
//!         and \b --print-unknown and performs the corresponding actions.
//!
//!
//! @param argc,argv
//!    arguments passed to <B>main(int argc, char **argv)</B>
//!
//! @param PrintHelp
//!    function that prints the help
//!
//! @returns
//!    A reference to the list with the resulting options with their
//!    values.
//!
//! @todo
//!    - describe the exceptions
//!    - describe what happens in a more general way
//!    - print a waring when no default coonfig file is read
//!    - proper handling and error messages if files not available
//
const po::variables_map &Configuration::parse(int argc, const char **argv,
    const std::function<void()> &PrintHelp) {
  const po::positional_options_description &opt_positional = fArgumentPositions;

  // ------------------------ (0) --------------------------
#ifdef DEBUG
  cout << "--0--" << endl;
#endif

  po::options_description opt_commandline;
  po::options_description opt_configfile;
  po::options_description opt_environment;
  po::options_description opt_database;

  for (int i = 0; i < 2; i++) {
    opt_commandline.add(fOptionsCommandline[i]);
    opt_configfile.add(fOptionsConfigfile[i]);
    opt_environment.add(fOptionsEnvironment[i]);
    opt_database.add(fOptionsDatabase[i]);
  }

  // ------------------------ (1) --------------------------
#ifdef DEBUG
  cout << "--1--" << endl;
#endif

  fPriorityFile = "";
  fDefaultFile = "";
  fDatabase = "";

  // ------------------------ (2) --------------------------
#ifdef DEBUG
  cout << "--2--" << endl;
#endif

  po::command_line_parser parser(argc, const_cast<char**>(argv));
  parser.options(opt_commandline);
  parser.positional(opt_positional);
  parser.style(style::unix_style & ~style::allow_guessing);
  //parser.allow_unregistered();

  const po::parsed_options parsed_commandline = parser.run();

  // ------------------------ (3) --------------------------
#ifdef DEBUG
  cout << "--3--" << endl;
#endif

  po::variables_map getfiles;
  po::store(parsed_commandline, getfiles);

  if (getfiles.count("version"))
    printVersion();
  if (getfiles.count("help")) {
    fPrintUsage();
    cout << "Options:\n"
        "The following describes the available commandline options. "
        "For further details on how command line option are parsed "
        "and in which order which configuration sources are accessed "
        "please refer to the class reference of the Configuration class."
        << endl;
    cout << fOptionsCommandline[kVisible] << endl;
  }
  if (getfiles.count("help-config"))
    cout << fOptionsConfigfile[kVisible] << endl;
  if (getfiles.count("help-env"))
    cout << fOptionsEnvironment[kVisible] << endl;
  if (getfiles.count("help-database"))
    cout << fOptionsDatabase[kVisible] << endl;

  // ------------------------ (4) --------------------------
#ifdef DEBUG
  cout << "--4--" << endl;
#endif

  if (getfiles.count("print") || getfiles.count("print-all")) {
    cout << endl << "Parsed commandline options:" << endl;
    printParsed(parsed_commandline);
    cout << endl;
  }

  if (getfiles.count("help") || getfiles.count("help-config")
      || getfiles.count("help-env") || getfiles.count("help-database")) {
    if (PrintHelp)
      PrintHelp();
  }

  // ------------------------ (5) --------------------------
#ifdef DEBUG
  cout << "--5--" << endl;
#endif

  const boost::filesystem::path path(getName());
  const string globalfile = (path.parent_path()
      / boost::filesystem::path("fact++.rc")).string();

  cerr << "Reading global  options from '" << globalfile << "'." << endl;

  ifstream gfile(globalfile.c_str());
  // ===> FIXME: Proper handling of missing file or wrong file name
  const po::parsed_options parsed_globalfile =
      !gfile ?
          po::parsed_options(&opt_configfile) :
          po::parse_config_file<char>(gfile, opt_configfile, true);

  // ------------------------ (6) --------------------------
#ifdef DEBUG
  cout << "--6--" << endl;
#endif

  // Get default file from command line
  if (getfiles.count("default")) {
    fDefaultFile = getfiles["default"].as<string>();
    cerr << "Reading default options from '" << fDefaultFile << "'." << endl;
  }

  const bool checkf = !getfiles.count("dont-check-files")
      && !getfiles.count("dont-check");
  const bool defaulted = getfiles.count("default")
      && getfiles["default"].defaulted();
  //const bool exists    = boost::filesystem::exists(fDefaultFile);

  ifstream indef(fDefaultFile.c_str());
  // ===> FIXME: Proper handling of missing file or wrong file name
  const po::parsed_options parsed_defaultfile =
      !indef && defaulted ?
          po::parsed_options(&opt_configfile) :
          po::parse_config_file<char>(indef, opt_configfile, !checkf);

  // ------------------------ (7) --------------------------
#ifdef DEBUG
  cout << "--7--" << endl;
#endif

  if (getfiles.count("print-default") || getfiles.count("print-all")) {
    if (!indef.is_open() && defaulted)
      cout << "No configuration file by --default option specified." << endl;
    else {
      cout << endl << "Parsed options from '" << fDefaultFile << "':" << endl;
      printParsed(parsed_defaultfile);
      cout << endl;
    }
  }

  po::store(parsed_defaultfile, getfiles);

  // ------------------------ (8) --------------------------
#ifdef DEBUG
  cout << "--8--" << endl;
#endif

  // Get priority from commandline(1), defaultfile(2)
  if (getfiles.count("config")) {
    fPriorityFile = getfiles["config"].as<string>();
    cerr << "Reading config options from '" << fPriorityFile << "'." << endl;
  }

  ifstream inpri(fPriorityFile.c_str());
  // ===> FIXME: Proper handling of missing file or wrong file name
  const po::parsed_options parsed_priorityfile =
      fPriorityFile.empty() ?
          po::parsed_options(&opt_configfile) :
          po::parse_config_file<char>(inpri, opt_configfile, !checkf);

  // ------------------------ (9) --------------------------
#ifdef DEBUG
  cout << "--9--" << endl;
#endif

  if (getfiles.count("print-config") || getfiles.count("print-all")) {
    if (fPriorityFile.empty())
      cout << "No configuration file by --config option specified." << endl;
    else {
      cout << endl << "Parsed options from '" << fPriorityFile << "':" << endl;
      printParsed(parsed_priorityfile);
      cout << endl;
    }
  }

  // ------------------------ (10) -------------------------
#ifdef DEBUG
  cout << "--10--" << endl;
#endif

  po::variables_map getdatabase;
  po::store(parsed_commandline, getdatabase);
  po::store(parsed_priorityfile, getdatabase);
  po::store(parsed_defaultfile, getdatabase);
  po::store(parsed_globalfile, getdatabase);

  if (getdatabase.count("database") && !getdatabase.count("no-database")) {
    fDatabase = getdatabase["database"].as<string>();
    cerr << "Requesting options from database for '" << fName << "'" << endl;
  }

  const bool checkdb = !getdatabase.count("dont-check-database")
      && !getdatabase.count("dont-check");

  const po::parsed_options parsed_database =
      fDatabase.empty() ?
          po::parsed_options(&opt_database) :
#if BOOST_VERSION < 104600
          parseDatabase(path.filename(), fDatabase, opt_database, !checkdb);
#else
          parseDatabase(path.filename().string(), fDatabase, opt_database,
              !checkdb);
#endif
  // ------------------------ (11) -------------------------
#ifdef DEBUG
  cout << "--11--" << endl;
#endif

  if (getfiles.count("print-database") || getfiles.count("print-all")) {
    if (fDatabase.empty())
      cout << "No database access requested." << endl;
    else {
      cout << endl << "Options received from '" << fDatabase << "':" << endl;
      printParsed(parsed_database);
      cout << endl;
    }
  }

  // ------------------------ (12) -------------------------
#ifdef DEBUG
  cout << "--12--" << endl;
#endif

  const po::parsed_options parsed_environment = po::parse_environment(
      opt_environment, fNameMapper);

  // ------------------------ (13) -------------------------
#ifdef DEBUG
  cout << "--13--" << endl;
#endif

  if (getfiles.count("print-environment")) {
    cout << "Parsed options from environment:" << endl;
    printParsed(parsed_environment);
    cout << endl;
  }

  // ------------------------ (14) -------------------------
#ifdef DEBUG
  cout << "--14--" << endl;
#endif

  po::variables_map result;
  po::store(parsed_commandline, result);
  po::store(parsed_priorityfile, result);
  po::store(parsed_database, result);
  po::store(parsed_defaultfile, result);
  po::store(parsed_globalfile, result);
  po::store(parsed_environment, result);
  po::notify(result);

  fVariables = result;

  // ------------------------ (15) -------------------------
#ifdef DEBUG
  cout << "--15--" << endl;
#endif

  const vector<string> unknown0 = collect_unrecognized(
      parsed_globalfile.options, po::exclude_positional);
  const vector<string> unknown1 = collect_unrecognized(
      parsed_defaultfile.options, po::exclude_positional);
  const vector<string> unknown2 = collect_unrecognized(
      parsed_priorityfile.options, po::exclude_positional);

  fUnknownConfigfile.clear();
  fUnknownConfigfile.insert(fUnknownConfigfile.end(), unknown0.begin(),
      unknown0.end());
  fUnknownConfigfile.insert(fUnknownConfigfile.end(), unknown1.begin(),
      unknown1.end());
  fUnknownConfigfile.insert(fUnknownConfigfile.end(), unknown2.begin(),
      unknown2.end());

  fUnknownCommandline = collect_unrecognized(parsed_commandline.options,
      po::exclude_positional);
  fUnknownEnvironment = collect_unrecognized(parsed_environment.options,
      po::exclude_positional);
  fUnknownDatabase = collect_unrecognized(parsed_database.options,
      po::exclude_positional);

  // ------------------------ (16) -------------------------
#ifdef DEBUG
  cout << "--16--" << endl;
#endif

  createWildcardOptions();

  // ------------------------ (17) -------------------------
#ifdef DEBUG
  cout << "--17--" << endl;
#endif

  if (result.count("print-options"))
    printOptions();

  if (result.count("print-wildcards"))
    printWildcardOptions();

  if (result.count("print-unknown"))
    printUnknown();

#ifdef DEBUG
  cout << "------" << endl;
#endif

  return fVariables;
}

bool Configuration::doParse(int argc, const char **argv,
    const std::function<void()> &PrintHelp) {
  try {
    parse(argc, argv, PrintHelp);
  }
#if BOOST_VERSION > 104000
  catch (po::multiple_occurrences &e) {
    cerr << "Program options invalid due to: " << e.what() << " of '"
        << e.get_option_name() << "'." << endl;
    return false;
  }
#endif
  catch (exception& e) {
    cerr << "Program options invalid due to: " << e.what() << endl;
    return false;
  }

  return !hasVersion() && !hasPrint() && !hasHelp();
}

// --------------------------------------------------------------------------
//
//! Create a list of all options which were registered using wildcards
//!
void Configuration::createWildcardOptions() {
  po::options_description opts;

  for (int i = 0; i < 2; i++) {
    opts.add(fOptionsCommandline[i]);
    opts.add(fOptionsConfigfile[i]);
    opts.add(fOptionsEnvironment[i]);
    opts.add(fOptionsDatabase[i]);
  }

  fWildcardOptions.clear();

  typedef map<string, po::variable_value> Vars;
  typedef vector<boost::shared_ptr<po::option_description>> Descs;

  const Descs &desc = opts.options();

  for (Vars::const_iterator io = fVariables.begin(); io != fVariables.end();
      ++io) {
    for (Descs::const_iterator id = desc.begin(); id != desc.end(); ++id)
#if BOOST_VERSION > 104000
      if ((*id)->match(io->first, false, false, false)
          == po::option_description::approximate_match)
#else
        if ((*id)->match(io->first, false)==po::option_description::approximate_match)
#endif
        fWildcardOptions[io->first] = (*id)->long_name();
  }
}

// --------------------------------------------------------------------------
//
//! Print a list of all options which were registered using wildcards and
//! have not be registered subsequently by access.
//!
void Configuration::printWildcardOptions() const {
  cout << "Options registered with wildcards and not yet accessed:" << endl;

  size_t max = 0;
  for (auto it = fWildcardOptions.begin(); it != fWildcardOptions.end(); it++)
    if (it->second.length() > max)
      max = it->second.length();

  cout.setf(ios_base::left);
  for (auto it = fWildcardOptions.begin(); it != fWildcardOptions.end(); it++)
    cout << setw(max + 1) << it->second << " : " << it->first << endl;
}

const vector<string> Configuration::getWildcardOptions(
    const std::string &opt) const {
  vector<string> rc;

  for (auto it = fWildcardOptions.begin(); it != fWildcardOptions.end(); it++) {
    if (it->second == opt)
      rc.push_back(it->first);
  }

  return rc;
}

// --------------------------------------------------------------------------
//
//! Removes /.libs/lt- from a path or just lt- from the filename.
//!
//! @param src
//!    input path with filename
//! @returns
//!    path cleaned from libtool extensions
//!
string Configuration::unLibToolize(const string &src) const {
  const boost::filesystem::path path(src);

  string pname = path.parent_path().string();
#if BOOST_VERSION < 104600
  string fname = path.filename();
#else
  string fname = path.filename().string();
#endif

  // If the filename starts with "lt-" remove it from the name
  if (fname.substr(0, 3) == "lt-")
    fname = fname.substr(3);

  // If no directory is contained determine the current directory
  if (pname.empty())
    pname = boost::filesystem::current_path().string();

  // If the directory is relative and just ".libs" forget about it
  if (pname == ".libs")
    return fname;

  // Check if the directory is long enough to contain "/.libs"
  if (pname.length() >= 6) {
    // If the directory ends with "/.libs", remove it
    const size_t pos = pname.length() - 6;
    if (pname.substr(pos) == "/.libs")
      pname = pname.substr(0, pos);
  }

  // If the path is the local path do not return the path-name
  if (pname == boost::filesystem::current_path().string())
    return fname;

  return pname + '/' + fname;
}

// --------------------------------------------------------------------------
//
//! Print version information about the program and package.
//!
//! The program name is taken from fName. If a leading "lt-" is found,
//! it is removed. This is useful if the program was build and run
//! using libtool.
//!
//! The package name is taken from the define PACKAGE_STRING. If it is
//! not defined (like automatically done by autoconf) no package information
//! is printed. The same is true for PACKAGE_URL and PACKAGE_BUGREPORT.
//!
//! From help2man:
//!
//! The first line of the --version information is assumed to be in one
//! of the following formats:
//!
//! @verbatim
//!  - \<version\>
//!  - \<program\> \<version\>
//!  - {GNU,Free} \<program\> \<version\>
//!  - \<program\> ({GNU,Free} \<package\>) \<version\>
//!  - \<program\> - {GNU,Free} \<package\> \<version\>
//! @endverbatim
//!
//!  and separated from any copyright/author details by a blank line.
//!
//! Handle multi-line bug reporting sections of the form:
//!
//! @verbatim
//!  - Report \<program\> bugs to \<addr\>
//!  - GNU \<package\> home page: \<url\>
//!  - ...
//! @endverbatim
//!
void Configuration::printVersion() const {
#ifndef PACKAGE_STRING
#define PACKAGE_STRING ""
#endif

#ifndef PACKAGE_URL
#define PACKAGE_URL ""
#endif

#ifndef PACKAGE_BUGREPORT
#define PACKAGE_BUGREPORT ""
#endif

  if (fPrintVersion) {
    fPrintVersion(fName);
    return;
  }

#if BOOST_VERSION < 104600
  const std::string n = boost::filesystem::path(fName).filename();
#else
  const std::string n = boost::filesystem::path(fName).filename().string();
#endif

  const string name = PACKAGE_STRING;
  const string bugs = PACKAGE_BUGREPORT;
  const string url = PACKAGE_URL;

  cout << n;
  if (!name.empty())
    cout << " - " << name;
  cout << "\n\n"
      "Written by Thomas Bretz et al.\n"
      "\n";
  if (!bugs.empty())
    cout << "Report bugs to <" << bugs << ">\n";
  if (!url.empty())
    cout << "Home page: " << url << "\n";
  cout << "\n"
      "Copyright (C) 2011 by the FACT Collaboration.\n"
      "This is free software; see the source for copying conditions.\n"
      << std::endl;
}

