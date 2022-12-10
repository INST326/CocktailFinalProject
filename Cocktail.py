import re
import pandas as pd
import seaborn as sns

class DataAnalysis:
    def __init__(self, cocktails_file, ingredients_file):
        self.cocktails = pd.read_csv(cocktails_file)# reads the csv
        self.ingredients = pd.read_csv(ingredients_file)# reads the csv

    def menu(self):
        self.cocktails.columns = ["Drink_name", "Ingredients", "Price"]# renamed the 3 columns
        self.cocktails.loc[-1] = ['Old Fashioned','whiskey,angostura bitters,water,simple syrup','29']# adds the row I had to replace
        change_to_num = self.cocktails.loc[:, "Price"]## separated to be able to change the rows to ints
        change_to_num = change_to_num.apply(pd.to_numeric, errors='coerce')## changed rows to ints
        self.cocktails.loc[:,"Price"] = change_to_num ## replaced the values
        cocktails_and_price = self.cocktails.loc[:, ['Drink_name', 'Price']].sort_values('Price', ascending=False)# decending
        print(cocktails_and_price)
        
    def amount_of_ingredients(self):
        self.ingredients = pd.read_csv("ingredients.csv")
        self.ingredients.columns = ["Ingredient", "Price", "Type"]# renamed the top columns
        self.ingredients.loc[-1] =  ['whiskey',4,'smokey']# added the one I renamed back
        type_and_amount = self.ingredients.value_counts("Type").to_frame("Amount").reset_index(0)# I counted the type of ingredients and added them to amount and reordered the numbers
        print(type_and_amount)
        
    def top_shelf_drinks(self): 
        top_shelf = self.cocktails.nlargest(5, 'Price')
        print(top_shelf)    
        
    def bottom_shelf_drinks(self): 
        bottom_shelf = self.cocktails.nsmallest(5,"Price")
        bottom_shelf
        
    def flavor_graph(self):
        type_and_amount = self.ingredients.value_counts("Type").to_frame("Amount").reset_index(0)# I counted the type of ingredients and added them to amount and reordered the numbers
        sns.set_palette([ "black", "#34495e"])# changed the style of seaborn to look better
        type_and_amount.plot(kind='bar', x='Type', y='Amount')# made the bar plot  
    def cocktail_graph(self):
        cocktails_and_price = self.cocktails.loc[:, ['Drink_name', 'Price']].sort_values('Price', ascending=False)# decending
        cocktails_and_price.plot(kind='bar', x='Drink_name', y='Price')

class Ingredient:
    """ A class that sets the name, price, and flavor of the ingredients.
  
       Attributes:
           name (str): name of ingredient
           price (float): price of ingredient
           flavor (str): flavor of ingredient
    """   
    def __init__(self, name, price, flavor) -> None:
        """Initializes the ingredients class.
 
        Args:
            name (str): Name of the ingredient.
            price (float): Price of the ingredients.
            flavor (str): Flavor type of the ingredients.
        """
        self.name = name
        self.price = price
        self.flavor = flavor

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
        
        return Cocktail(f"{self.name} x {other.name}", 
        self.ingredients.union(other.ingredients))
 
 
        
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
          
        ingr_txt = ", ".join([ingr.name for ingr in self.ingredients])
        return f"{self.name} - ${self.price()}"
  
    def __repr__(self) -> str:
        """Returns the object representation of the string format for the cocktails.
        Returns:
            str: Returns the objects of the cocktails.
        """    
        
        return f"Cocktail(${self.name!r})"
  
    
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
        
        #Bohan add with statement here
        
        if "cocktails" in filepath:
            regex = r"(?P<Name>[^,]+),[\"](?P<Ingredients>[^\"]+)[\"],(?P<Strength>[\d.]+)"
            match = re.search(regex, line)
            name = match.group("Name")
            ingredients = match.group("Ingredients")
            strength = match.group("Strength")
            ingredients_split = ingredients.split(",")
            ingr_list = [self.ingr[ingr_iter] for ingr_iter in ingredients_split]
            self.cocktails[name] = Cocktail(name, ingr_list, float(int(strength) * 0.01))
            
        elif "ingredients" in filepath:
            regex = r"(?P<Name>[^,]+),(?P<Price>[\d.]+),(?P<Flavor>[a-zA-Z]+)"
            match = re.search(regex, line)
            name, price, flavor = match.groups()
            self.ingr[name] = Ingredient(name, int(price), flavor)
                                            
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

def handle_dialogue(bar):
    """Handle the input dialogue for user to interact with Bar object

    Args:
        bar (Bar): a Bar object that we are ordering from
        
    Side effects:
        Printing to stout
    """
    
    while (True):
        #Nick starts dialogue
        action = input(f"Welcome to {bar.name}. What can I do for you? \n 1: Order a cocktail \n 2: Recommend cocktails \n 3: Create a cocktail\n")
        
        if int(action) == 1:
            sorted_cocktails = {k: v for k, v in sorted(bar.cocktails.items(), key=lambda item: item[1])}
            cocktail_list = [ f"{index}: {str(cocktail)}" for (index, cocktail) in enumerate(sorted_cocktails.values()) ]
            order_number = input(f"Great! Here's a list of our cocktails. \n {cocktail_list} \n")
            bar.order(list(sorted_cocktails.keys())[int(order_number)])
            orders_joined = ",".join([order.name for order in bar.myorder])
            print(f"Excellent choice! Here are your orders: {orders_joined} \nYour total is: ${bar.tab()}")
            
        elif int(action) == 2:
            flavor_list = [ f"{index}: {flavor}" for (index, flavor) in enumerate(bar.get_flavors()) ]
            flavor_input = input(f"What flavor would you like. {flavor_list} \n")
            recommended = bar.recommend_cocktails(bar.get_flavors()[int(flavor_input)])
            recommended_text = ", ".join([rec.name for rec in recommended])
            print(f"Here's what we found: {recommended_text} \n")
        
        elif int(action) == 3:
            ingr_list = [ f"{index}: {ingr.name}" for (index, ingr) in enumerate(bar.ingr.values()) ]
            cocktail_name = input("What should we name your cocktail? \n")
            print(f"Now lets add some ingredients. Here's what we have. \n{ingr_list}")
            selected_ingrs = input("Use the following format: 1,5,4 \n")
            selected_ingrs = selected_ingrs.split(",")
            ingrs = [list(bar.ingr.values())[int(index)] for index in selected_ingrs]
            bar.create_cocktail(cocktail_name, ingrs)
            print(f"Your cocktail has been added to the menu!")
 
 

