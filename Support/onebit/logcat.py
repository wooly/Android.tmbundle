import onebit
import os

template = onebit.env.get_template("logcat.html")

print template.render(
    title='Logcat', 
)