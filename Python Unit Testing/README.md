# Unit testing in Python

### What is unit testing?
-Unit Testing is the first level of software testing where the smallest testable parts of a software are tested.


##### Popular Python Libraries for unit testing:
 - `unittest(PyUnit)`
 - `doctest`
 - `PyTest`

### OOP concepts for unit testing:

- `text fixture`:  baseline for running tests to ensure that there is a fixed environment in which tests are run so that results are repeatable.
- `test case`: set of conditions which is used to determine whether a system under test works correctly
- `test suite`: collection of testcases that are used to test a software program to show that it has some specified set of behaviours by executing the aggregated tests together.
- `test runner`: component which set up the execution of tests and provides the outcome to the user.


##### Basic terms used in the code:

- `assertEqual()`: This statement is used to check if the result obtained is equal to the expected result.
- `assertTrue() / assertFalse()`: This statement is used to verify if a given statement is true or false.
- `assertRaises()`: This statement is used to raise a specific exception.

##### Description of tests:

- `test_strings_a`: This test is used to test the property of string in which a character say ‘a’ multiplied by a number say ‘x’ gives the output as x times ‘a’. The assertEqual() statement returns true in this case if the result matches the given output.
- `test_upper`: This test is used to check if the given string is converted to uppercase or not. The assertEqual() statement returns true if the string returned is in uppercase.
- `test_isupper`: This test is used to test the property of string which returns TRUE if the string is in uppercase else returns False. The assertTrue() / assertFalse() statement is used for this verification.
- `test_strip`: This test is used to check if all chars passed in the function have been stripped from the string. The assertEqual() statement returns true if the string is stripped and matches the given output.
- `test_split`: This test is used to check the split function of the string which splits the string through the argument passed in the function and returns the result as list. The assertEqual() statement returns true in this case if the result matches the given output.
