class Cocktail:
        
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