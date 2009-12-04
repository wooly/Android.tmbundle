import onebit
import os

template = onebit.env.get_template("installapp.html")

print template.render(
    title='Install Android App', 
)

