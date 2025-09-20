# Adding newlines (\n) and tabs (\t)
print("Languages:\n\tPython\n\tC++\n\tJavaScript")

print("\n--- Now stripping whitespace ---")

# Stripping whitespace
favorite_language = "  python  "
print(f"'{favorite_language}'")
print(f"'{favorite_language.rstrip()}'") # Strips from the right
print(f"'{favorite_language.lstrip()}'") # Strips from the left
print(f"'{favorite_language.strip()}'")  # Strips from both sides