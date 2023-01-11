# #!/usr/bin/env python3
#
# print("Content-type: text/html")
# print("""<!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta http-equiv="X-UA-Compatible" content="IE=edge">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#
#     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
#     <script defer src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
# </head>
# <body>
#     <form action="/cgi-bin/handlers/show_script.py">
#         <div class="form-group">
#           <label for="name">Shop name</label>
#           <input type="text" class="form-control" id="name" name="name" placeholder="Enter shop name">
#         </div>
#         <button type="submit" class="btn btn-primary">Show</button>
#     </form>
# </body>
# </html>""")



#!/usr/bin/env python3

print("Content-type: text/html")
print("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <script defer src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
</head>
<body>
    <form action="/cgi-bin/handlers/show_script.py">
        <div class="form-group">
          <label for="name">Manufacturer: </label>
          <input type="text" class="form-control" id="name" name="name" placeholder="Enter manufacturer: ">
        </div>
        <div class="form-group">
          <label for="model">Model: </label>
          <input type="text" class="form-control" id="model" name="model" placeholder="Enter model: ">
        </div>
        <button type="submit" class="btn btn-primary">Show</button>
    </form>
</body>
</html>""")