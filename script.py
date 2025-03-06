import sys
from string import Template

def main():
    # We can create a new template and parse its body from
    # a string.
    # Templates are a mix of static text and placeholders enclosed in
    # ${...} that are used to dynamically insert content.

    file_path = "test.template"

    with open(file_path, 'r') as file:
        file_content = file.read()

    t1 = Template(file_content)

    #  t1 = Template("Value is ${value}\n")

    # By "substituting" the template we generate its text with
    # specific values for its placeholders. The ${value} placeholder
    # is replaced by the value passed as a parameter to `substitute`.
    # print(t1.substitute(value="some text"))
    # print(t1.substitute(value=5))
    print(t1.substitute(xxx=["Python"]))

    # Helper function we'll use below.
    def create(template_string):
        return Template(template_string)

    # If the data is a dictionary we can use the ${key} placeholder to access
    # its values.
    t2 = create("Name: ${name}\n")

    print(t2.substitute({"name": "Jane Doe"}))

    # The same applies to objects; with objects we use the attribute names.
    class Person:
        def __init__(self, name):
            self.name = name

    print(t2.substitute(name=Person("Mickey Mouse").name))

    # Python's string.Template doesn't have built-in conditional logic,
    # but we can achieve similar results using string formatting or f-strings.
    def conditional_template(value):
        return "yes" if value else "no"

    print(f"{conditional_template('not empty')}\n")
    print(f"{conditional_template('')}\n")

    # For looping through lists, we can use list comprehension or join.
    t4 = create("Range: ${items}\n")
    items = ["Python", "Java", "C++", "C#"]
    print(t4.substitute(items=" ".join(items)))

if __name__ == "__main__":
    main()