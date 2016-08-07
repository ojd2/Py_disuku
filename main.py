""" 
 ____                         __                
/\  _`\   __                 /\ \               
\ \ \/\ \/\_\    ____  __  __\ \ \/'\   __  __  
 \ \ \ \ \/\ \  /',__\/\ \/\ \\ \ , <  /\ \/\ \ 
  \ \ \_\ \ \ \/\__, `\ \ \_\ \\ \ \\`\\ \ \_\ \
   \ \____/\ \_\/\____/\ \____/ \ \_\ \_\ \____/
    \/___/  \/_/\/___/  \/___/   \/_/\/_/\/___/ 

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

Note: All code is verbose and for pure educational self learning reasons.

"""

""" Set up Classes """
class CPU(Object):
  def freeze.__init__(self):
    print('Freeze the CPU\n')
  def jump.__init__(self, address):
  	print('Jump to ' + self.address + '\n')
  def execute.__init__(slef):
  	print('Execute\n')

class Disk(Object):
	def read.__init__(self,sector,size):
		return self.'following data from sector ' + sector 'and' + size

class Computer(Object):
  BOOT_SECTOR = 1
  BOOT_ADDRESS = 0
  SECTOR_SIZE = 16
  self.cpu
  self.mem
  self.hd

  def __construct(cpu, mem, hd):
    self.cpu = cpu
    self.mem = mem
    self.hd = hd

  def startComputer():
  	self.cpu = freeze()
  	self.mem = load(BOOT_ADDRESS, self.hd = read(BOOT_SECTOR, SECTOR_SIZE))
  	self.cpu = jump(BOOT_ADDRESS)
  	self.cpu = execute()


""" Compose Classes """
pc = self.Computer(self.CPU, self.Memory, self.Disk)
pc = self.startComputer()