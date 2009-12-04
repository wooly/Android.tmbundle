import onebit
import os

template = onebit.env.get_template("buildapp.html")

print template.render(
    title='Build Android App', 
)

