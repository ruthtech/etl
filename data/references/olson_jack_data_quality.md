# "Data Quality: The Accuracy Dimension" by Jack E. Olson 
## Published by Morgan Kaufmann. 2003. Appendix B.


--- 
### Content of a Data Profiling Repository
1. Schema Definition
2. Business Objects
3. Domains
4. Data Source
5. Table Definitions
6. Synonyms
7. Data Rules
8. Value Rules
9. Issues

--- 
### Schema Definition
* Identification of the collection of data that is profiled together
* Business description
* Data steward
* Business analysts with knowledge of objects

--- 
### Business Objects
* Name
* Business description
* Tables used to store object data
* Data model of business object

--- 
### Domains
* Name
* Description
* Data type
* Length boundaries
* Numeric precision
* Value properties
* Discrete  value list
  * Encoded value meanings 
  * Range of values permitted
    * Skip-over rule   
  * Character patterns required   
  * Character set   
  * Character exclusions 
  * Text field restrictions

---
### Data Source
* Type IMS/VSAM/ORACLE/...
* Physical location
* Application name
* Application description
* Database administrator name
* Key dates
  * First deployment date
  * Major change dates
* Extraction information
  * Data conversions needed
  * Overloaded field definitions
* Tables that result from extraction
* Extraction executions
  * Date of extraction
  * Type full or sample

---
### Table Definitions
* Name
* Descriptive name
* Business meaning
* Columns
  * Name
  * Longer descriptive name
  * Business definition
  * Confidence indicators
    * Trusted
    * Susceptibility to decay
    * Enforcement processes
  * Domain names if inherited
  * Data type
    * Data type discovered
  * Length boundaries
    * Maximum length discovered
    * Minimum length discovered
    * Length distributions discovered
  * Numeric precision
    * Maximum precision discovered
  * Value properties
    * Discrete value list
      * Values discovered
      * Inaccurate values
      * Values not used
      * Encoded value meanings
    * Range of values permitted
    * Skip-over rule
      * Skip-over rule violations
    * Character patterns required
      * Patterns discovered
    * Character set
    * Character exclusions
    * Text field restrictions
      * Keywords discovered
      * Text constructs discovered (embedded blanks, special characters)
      * Upper/lowercase conventions discovered
      * Leading/trailing blanks discovered
    * Property rules
      * Unique rule
        * Uniqueness percentage discovered
      * Null rule
        * Null indications
          * Null indications discovered
          * Blank or zero rule
      * Inconsistency points
        * Date of change
        * Description of change
    * Functional dependencies
      * LHS columns
      * RHS columns
      * Type
        * Primary key
          * Token
          * Natural
          * Denormalized key
          * Derived column
            * Rule or formula
        * Discovered percentage true
          * Violation values

---
### Synonyms
* Primary table and columns
* Secondary table and columns
* Type
* Primary key/foreign key  
* Redundant 
* Domain  
* Merge  
* Value correspondence  
  * Same  
  * Transform  
* Inclusivity  
  * Inclusive 
  * Bidirectional  inclusive  
  * Exclusive  
  * Mixed  
* Degree  of overlap  
    * One-to-one  
    * One-to-many  
    * Many-to-many  
    * Value lists  
    * Violation data

---
### Data Rules 
* Name of rule 
* Description of business meaning   
* Table names and column names used   
* Execution logic   
  * Rule logic expression or program or procedure name   
* Execution results   
  * Date  executed   
  * Number of rows   
  * RowID  list of violations with data   
* Remedy implementation   
  * Date/time implemented   
  * Type of implementation   
    * Data entry   
    * Transaction program   
    * Database-stored procedure   
    * Periodic checker execution   
    * Business process procedure

---
### Value Rules 
* Name of rule   
* Description of business meaning   
* Table names and  column names used   
* Execution logic   
  * Rule logic expression or program or procedure name   
* Result expectations   
* Execution results   
  * Date executed   
  * Number of rows   
  * RowlD  list of violations with data 
* Remedy implementation 
  * Date/time implemented   
  * Type of implementation   
    * Data entry   
    * Transaction program   
    * Database-stored procedure   
    * Periodic checker execution   
    * Business process procedure
  
---
### Issues
* Date/time created 
* Description of problem 
* Supporting evidence   
  * Column properties violations   
  * Structure analysis violations   
  * Data rule violations   
  * Value rule violations   
* Remedies recommended   
* Remedies accepted   
* Remedies implemented   
* Evidence supporting improvements   
  * Reduction in violations

