# Family Tree

Given an input text file, the code does the following :

  - Initializes Lengaburu family tree (as given in the question)
  - Given a ‘name’ and a ‘relationship’, the code outputs the people corresponding to the relationship in the order in which they were added to the family tree. 
  - Any new member (child) can be added to any family in the tree through the mother.

### Solution Overview

  - **Person Class** 
    Stores the personal characteristics of a Person in a Family and also responsible for returning various attributes corresponding to a person 
  - **FamilyTree Class**
    Stores the entire Family Tree and is responsible for populating the tree contents
  - **GetRelationship Class**
    Gets the various relationships of the members

### Valid Relationships the Solution can handle

  - **Paternal-Uncle** 
  - **Paternal-Aunt**
  - **Maternal-Uncle**
  - **Maternal-Aunt**
  - **Sister-In-Law**
  - **Brother-In-Law**
  - **Son**
  - **Daughter**
  - **Siblings**

### Supported Operation Types
```sh
$ ADD_CHILD "mother'name" "child's name" "child's gender"
$ GET_RELATIONSHIP "name" "relationship"
```
### Sample Input File
```sh
$ ADD_CHILD Satya Ketu Male
$ GET_RELATIONSHIP Kriya Paternal-Uncle
```
 
### Output terminology

  - **None** 
    If no relations are found corresponding to a particular relationship
  - **PERSON_NOT_FOUND**
    If a person does not exist in the FamilyTree 
  - **CHILD_ADDITION_FAILED**
    If an attempt to add a child is being made via the father
  - **CHILD_ADDITION_SUCCEEDED**
    If an attempt to add a child is being made via the mother

### Execution
Use the following command to execute. **geektrust** is the file containing the main method.

```sh
$ pip install -r requirements.txt
$ python -m geektrust <absolute_path_to_input_file>
```

### Tests
All the tests have been placed inside the tests module,for running the tests use **tests** module.
Sample command to run the tests:
```sh
$ python -m unittest
```

Please Note: There are no specific requirements other than Python. The code is develpoed using Python **3.7.3**.

### Future Scope
Any new relationship can be added to the GetRelationship class and accordingly in the Person or FamilyTree Class

# Family Tree

Given an input text file, the code does the following :

  - Initializes Lengaburu family tree (as given in the question)
  - Given a ‘name’ and a ‘relationship’, the code outputs the people corresponding to the relationship in the order in which they were added to the family tree. 
  - Any new member (child) can be added to any family in the tree through the mother.

### Solution Overview

  - **Person Class** 
    Stores the personal characteristics of a Person in a Family and also responsible for returning various attributes corresponding to a person 
  - **FamilyTree Class**
    Stores the entire Family Tree and is responsible for populating the tree contents
  - **GetRelationship Class**
    Gets the various relationships of the members

### Valid Relationships the Solution can handle

  - **Paternal-Uncle** 
  - **Paternal-Aunt**
  - **Maternal-Uncle**
  - **Maternal-Aunt**
  - **Sister-In-Law**
  - **Brother-In-Law**
  - **Son**
  - **Daughter**
  - **Siblings**

### Supported Operation Types
```sh
$ ADD_CHILD "mother'name" "child's name" "child's gender"
$ GET_RELATIONSHIP "name" "relationship"
```
### Sample Input File
```sh
$ ADD_CHILD Satya Ketu Male
$ GET_RELATIONSHIP Kriya Paternal-Uncle
```
 
### Output terminology

  - **None** 
    If no relations are found corresponding to a particular relationship
  - **PERSON_NOT_FOUND**
    If a person does not exist in the FamilyTree 
  - **CHILD_ADDITION_FAILED**
    If an attempt to add a child is being made via the father
  - **CHILD_ADDITION_SUCCEEDED**
    If an attempt to add a child is being made via the mother

### Execution
Use the following command to execute. **geektrust** is the file containing the main method.

```sh
$ pip install -r requirements.txt
$ python -m geektrust <absolute_path_to_input_file>
```

### Tests
All the tests have been placed inside the tests module,for running the tests use **tests** module.
Sample command to run the tests:
```sh
$ python -m unittest
```

Please Note: There are no specific requirements other than Python. The code is develpoed using Python **3.7.3**.

### Future Scope
Any new relationship can be added to the GetRelationship class and accordingly in the Person or FamilyTree Class
