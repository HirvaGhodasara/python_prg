# 1. GLOBAL VARIABLE
# Defined at the top level; accessible everywhere.
count = 10 

def outer_function():
    # 2. LOCAL VARIABLE
    # Defined inside a function; accessible only here.
    # This creates a NEW variable 'count' specific to this function,
    # distinct from the global 'count'.
    count = 20
    
    def inner_function():
        # 3. NONLOCAL VARIABLE
        # The 'nonlocal' keyword allows us to modify the variable 
        # in the nearest enclosing scope (outer_function).
        nonlocal count
        count = 30
        print(f"Inside inner_function (Nonlocal): {count}")

    print(f"Inside outer_function (Before call): {count}")
    inner_function()
    print(f"Inside outer_function (After call):  {count}")

# --- Execution ---
print(f"Global Scope (Start):                {count}")
outer_function()
print(f"Global Scope (End):                  {count}")
