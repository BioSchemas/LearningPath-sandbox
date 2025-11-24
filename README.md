# Learning Path sandbox

authors: Phil Reed, Alban Gaignard

drafted the 20th of November 2025, as part of Bioschemas activities

To be revised by the community.

Any questions, please contact phil.reed@manchester.ac.uk, alban.gaignard@univ-nantes.fr

## Aim of the repo
Report experiments to model Learning Paths with Schema.org ontology. 

## Content 

A jupyter notebook showing :
 - How Schema.org can be used, especially the HowTo, HowToSection, and HowToStep types and the required properties to properly define order between steps.
 - Some code to query (SPARQL and property path) the semantic annotations and retrieve for a given step the learning prerequesites.
 - Some code to transform Schema.org markup into a Mermaid diagram

## Results 
A sample Learning path: 
```turtle
ex:GA_learning_path a schema:Course,
        schema:HowTo ;
    schema:courseCode "GSA101" ;
    schema:description "A foundational course for Galaxy and Sequence analysis." ;
    schema:name "Introduction to Galaxy and Sequence analysis" ;
    schema:provider ex:ExampleUniversity ;
    schema:step ex:Module_1,
        ex:Module_2 .

ex:Module_1 a schema:Course,
        schema:HowToSection ;
    schema:itemListElement ex:TM11,
        ex:TM12,
        ex:TM3 ;
    schema:name "Module 1" ;
    schema:nextItem ex:Module_2 .

ex:TM11 a schema:HowToStep,
        schema:LearningResource ;
    schema:description "Description of TrainingMaterial 11" ;
    schema:name "TrainingMaterial 11" ;
    schema:nextItem ex:TM12 ;
    schema:url "https://tess.elixir-europe.org/materials/hands-on-for-a-short-introduction-to-galaxy-tutorial?lp=1%3A1" .

ex:TM12 a schema:HowToStep,
        schema:LearningResource ;
    schema:description "Description of TrainingMaterial 12" ;
    schema:name "TrainingMaterial 12" ;
    schema:nextItem ex:Module_2,
        ex:TM21,
        ex:TM3 .
```

And the complete diagram: 
```mermaid
graph TD
N1["Module 1"]
N9["TrainingMaterial shared by Module 1 and 2"]
N1 -- itemListElement --> N9
N2["Module 2"]
N5["TrainingMaterial 21"]
N2 -- itemListElement --> N5
N2["Module 2"]
N8["TrainingMaterial 24"]
N2 -- itemListElement --> N8
N4["TrainingMaterial 12"]
N9["TrainingMaterial shared by Module 1 and 2"]
N4 -- nextItem --> N9
N0["Introduction to Galaxy and Sequence analysis"]
N2["Module 2"]
N0 -- step --> N2
N4["TrainingMaterial 12"]
N2["Module 2"]
N4 -- nextItem --> N2
N1["Module 1"]
N2["Module 2"]
N1 -- nextItem --> N2
N7["TrainingMaterial 23"]
N8["TrainingMaterial 24"]
N7 -- nextItem --> N8
N5["TrainingMaterial 21"]
N6["TrainingMaterial 22"]
N5 -- nextItem --> N6
N2["Module 2"]
N6["TrainingMaterial 22"]
N2 -- itemListElement --> N6
N3["TrainingMaterial 11"]
N4["TrainingMaterial 12"]
N3 -- nextItem --> N4
N4["TrainingMaterial 12"]
N5["TrainingMaterial 21"]
N4 -- nextItem --> N5
N2["Module 2"]
N7["TrainingMaterial 23"]
N2 -- itemListElement --> N7
N8["TrainingMaterial 24"]
N9["TrainingMaterial shared by Module 1 and 2"]
N8 -- nextItem --> N9
N6["TrainingMaterial 22"]
N7["TrainingMaterial 23"]
N6 -- nextItem --> N7
N2["Module 2"]
N9["TrainingMaterial shared by Module 1 and 2"]
N2 -- itemListElement --> N9
N1["Module 1"]
N4["TrainingMaterial 12"]
N1 -- itemListElement --> N4
N1["Module 1"]
N3["TrainingMaterial 11"]
N1 -- itemListElement --> N3
N0["Introduction to Galaxy and Sequence analysis"]
N1["Module 1"]
N0 -- step --> N1
```

## Schema structure

We propose two new Bioschemas profiles and a small change to one Bioschemas profile:

- `LearningPath`: inherits from `Course` and `HowTo`
- `LearningPathTopic`: inherits from `Course` and `HowToSection`
- `TrainingMaterial`: inherits from `LearningResource` and `HowToStep`

A `LearningPath` has one or more `LearningPathTopic`. A `LearningPathTopic` has one or more `TrainingMaterial`. These relationships are (ordered) lists or steps, using the `HowTo` Schema.org type.

Class diagram:
```mermaid
classDiagram
direction TB
    class HowTo {
        step
    }
    class Course {
    }
    class LearningPath {
        LearningPathTopic[] step
    }
    class ItemList {
        itemListElement
    }
    class ListItem {
	    nextItem
    }
    class HowToSection {	    
    }
    class LearningPathTopic {
        TrainingMaterial[] itemListElement
        LearningPathTopic nextItem
    }
    class HowToStep {
    }
    class LearningResource {
    }
    class TrainingMaterial {
        TrainingMaterial nextItem
    }
    Course <|-- LearningPath
    Course <|-- LearningPathTopic
    ItemList <|-- HowToSection
    ListItem <|-- HowToSection
    ListItem <|-- HowToStep
    HowTo <|-- LearningPath
    HowToSection <|-- LearningPathTopic
    HowToStep <|-- TrainingMaterial
    LearningResource <|-- TrainingMaterial
```
