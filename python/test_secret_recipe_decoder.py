from secret_recipe_decoder import decode_ingredient, decode_string, Ingredient

def test_decode_string_can_decode():
    assert(decode_string("8 vgl") == "1 cup")

def test_decode_ingredient_can_decode():
    expected = Ingredient("1 cup", "butter")
    actual = decode_ingredient("8 vgl#hgiikf")
    assert(actual.amount == expected.amount)
    assert(actual.description == expected.description)
    
    
#Test the Functions
# Test decode_string function
print(decode_string("hgiikf"))  # Expected: "butter"
print(decode_string("8 vgl"))    # Expected: "1 cup"

# Test decode_ingredient function
ingredient = decode_ingredient("8 vgl#hgiikf")
print(ingredient.amount)         # Expected: "1 cup"
print(ingredient.description)    # Expected: "butter"

ingredient = decode_ingredient("8 ikyolnnq#jyqawwy")
print(ingredient.amount)         # Expected: "1 tablespoon"
print(ingredient.description)    # Expected: "vanilla"


# Run tests
test_decode_string_can_decode()
test_decode_ingredient_can_decode()
print("All tests passed!")