#### design software 

#### programming
* programmers combine primitive elements to form compound objects, they abstract compound objects to form higher-level building blocks, and they preserve modularity by adopting appropriate large-scale views of system structure.  
    - primitives -> compound objects -> higher-level blocks -> module -> system  

* Metalinguistic abstraction — establishing new languages  
    - Establishing new languages is a powerful strategy for controlling complexity in engineering design  
    - enhance our ability to deal with a complex problem by adopting a new language that enables us to **describe (and hence to think about) the problem in a different way**, using primitives, means of combination, and means of abstraction that are particularly well suited to the problem at hand  



#### JS  
* Module design    
    - ini package  

* data structures  
    - primitive values: num, booleans, strings 
        + immutable and cannot be changed  
        +  copied "as a whole value" 

    - arrays and objects are used to group values into a single value  
        + arrays  - sequence of values  
        + objects - dict  
            + reference  - binding 
            + mutable  
        + object is stored and copied "by **reference**"  
        
        + most objects also have a **prototype**  
            + a prototype is another object that is used as a fallback source of properties  
            + Object.prototype  

    
* JS functions are regular **values** **representing an "action"**     
    - higher-order functions allow us to **abstract over actions**, not just values  
        + pass function values to other functions  

* OOP  
    - divide programs into smaller pieces and **make each piece responsible for managing its own state**  
    - different pieces interact with each other through **interfaces**  
        + pieces are modeled using objects  
        + their interface consists of a specific set of methods and properities  

    - encapsulation  
        + separate interface from implementation     


* class  
    - in JS, a class is a kind of function  
    - a class is an **extensible program-code-template** for creating objects,
    providing init values for state (variables) and implementations of behavior (functions)



#### reference  
* [JavaScript The Good Parts] 
