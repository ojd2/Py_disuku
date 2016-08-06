```
 ____                         __                
/\  _`\   __                 /\ \               
\ \ \/\ \/\_\    ____  __  __\ \ \/'\   __  __  
 \ \ \ \ \/\ \  /',__\/\ \/\ \\ \ , <  /\ \/\ \ 
  \ \ \_\ \ \ \/\__, `\ \ \_\ \\ \ \\`\\ \ \_\ \
   \ \____/\ \_\/\____/\ \____/ \ \_\ \_\ \____/
    \/___/  \/_/\/___/  \/___/   \/_/\/_/\/___/ 
```

Recent changes in type classes within Python have seen 'new-style' classes
and 'old-style-classes' use different syntax. Now, "the class type is 
determined by the type of class(es) the class inherits from". So, in order
to apply the following rule, if no super classes are initiated within the 
source, subsequently this parses old-style class inheritance. 

However, as of Python 3.0, all classes are by default to be initiated as
new-style. As a result, the following application is a verbose and small
generic class composition experiment known as Disuku.  

Note: New-style classes have these features which old-style classes don't:
    
    * Universal base class called object.
    * Descriptors and properties. 

Note: If a class inherits from multiple parents which in turn inherit from 
a common grandparent, then when checking for an attribute or method, all 
parents will be checked before the grandparent.

Note: ```All code is verbose and for pure educational self learning reasons.```