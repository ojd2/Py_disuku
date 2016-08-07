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

More information to come.

```
Copyright © 2016 ojd2

Permission is hereby granted, free of charge, to any person obtaining a 
copy of this software and associated documentation files (the “Software”), 
to deal in the Software without restriction, including without limitation 
the rights to use, copy, modify, merge, publish, distribute, sublicense, 
and/or sell copies of the Software, and to permit persons to whom the 
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, 
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF 
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY 
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, 
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE 
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

```