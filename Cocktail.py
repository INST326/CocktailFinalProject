class Cocktail:
 
   """ A class that allows you to build cocktails with ingredients.
       Attributes:
           name (str): ingredients in the bar
           ingredients (set): The ingredients in the cocktail
           strength (float): percentage of abv
       Methods:
           price(): returns the total price of the cocktail
           flavors(): returns set of cocktail flavors
           ingredients_name(): returns set of cocktail ingredients
           str (): magic method that returns informal rep of cocktail
           repr(): megic method that returns formal rep of cocktail
           add (other): magic method adds two cocktail ingredients
           sub (other): magic method to get difference
                            between two cocktails ingredients
   """
 
   def __init__(self, name, ingredients, strength=None) -> None:
       pass
 
   def __add__(self, other):
       """ Returns new cocktail with ingredients in both.
           other(Cocktail): other cocktail to be combined with self.
           Returns:
               Cocktail: new cocktail with ingredients of combined.
       """
       pass
      
   def price(self) -> float:
       """Returns the price of the cocktail.
       Returns:
           float: The total cost
       """    
       pass  
  
   def flavors(self):
       """Returns the flavors of the cocktails.
       Returns:
           set: The flavors of the cocktails.
       """       
       return {i.flavor for i in self.ingredients}
  
   def ingredients_name(self):
       """Returns the ingredients name in the cocktails.
       Returns:
           set: the ingredients names of the cocktails.
       """  
       pass    
 
   def __str__(self) -> str:
       """Returns the string representation of the cocktails.
       Returns:
           str: String of the cocktails.
       """       
       pass
  
   def __repr__(self) -> str:
       """Returns the object representation of the string format for the cocktails.
       Returns:
           str: Returns the objects of the cocktails.
       """    
       pass  
  
   def __lt__(self, other):
       """Check less than for sorting
       Args:
          
       Returns:
           bool: is the cocktails price less than other
       """
      
       pass

class Bar:
   """Gathers the Cocktails and Ingredients classes to be able to recommend
       cocktails, ingredients,and load cocktails.
      
       Attributes:
           ingr (dict): ingredients in the bar
           cocktails (dict): cocktails in the bar
           myorder (list): list of ordered cocktails
  
       Methods:
           create_cocktail (name, ingredients): Creates new cocktail
           recommend_cocktails (flavor): Recommends cocktail based on flavor
           load_ingredients (filepath): Loads ingredients from file
           load_cocktails (filepath): Loads cocktails from file
           order (cocktail_name): Adds cocktail to order
           tab(): Returns current total price
           __str__ (): magic method that returns informal rep of bar
           __repr__(): magic method that returns formal rep of bar
   """   
   def __init__(self, name) -> None:
       """Initializes the Bar class.
           Attributes:
               ingr(dict): ingredients in the bar
               cocktails(dict): cocktails in the bar
               myorder(list): list of ordered cocktails
       """  
  
   def create_cocktail(self, name, ingredients):
       """ Adds a new cocktail to the bar.
 
           name(str): Name of cocktail
           ingredients(set): Ingredients of cocktail
       """
 
   def recommend_cocktails(self, flavor):
       """Returns the recommended cocktails based on the flavor.
 
       Args:
           flavor (str): The flavor of the cockatils
 
       Returns:
           list: The cocktails of the cocktails that it can recommend
       """       
 
   def load_data(self, filepath):
       """ loads ingredients from file into bar.
           filepath(str): Path to csv where ingredients are stored
          
           Side effect:
               Adds ingredients to self.ingr
       """
                                          
   def order(self, order):
       """ Creates an order of the cocktails served.
 
       Args:
           cocktail_name (str): Name of the cocktail served.
       """
      
   def tab(self):
       """Created a tab for the user to see how much everything will cost.
 
       Returns:
           float: The sum of all the drinks ordered.
       """       
  
   def get_flavors(self):
        pass
  
   def __str__():
       """  magic method that returns informal rep of bar
       """
       pass
  
   def __repr__():
       """ magic method that returns formal rep of bar
       """
       pass

