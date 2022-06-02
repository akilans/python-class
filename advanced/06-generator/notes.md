Let's say you have 100 million domains in your MySQL table, and you would like to update Alexa rank for each domain.

First thing you need is to select your domain names from the database.

Let's say your table name is domains and column name is domain.

If you use SELECT domain FROM domains it's going to return 100 million rows which is going to consume lot of memory. So your server might crash.

So you decided to run the program in batches. Let's say our batch size is 1000.

In our first batch we will query the first 1000 rows, check Alexa rank for each domain and update the database row.

In our second batch we will work on the next 1000 rows. In our third batch it will be from 2001 to 3000 and so on.

Now we need a generator function which generates our batches.

Here is our generator function:

```python
def ResultGenerator(cursor, batchsize=1000):
    while True:
        results = cursor.fetchmany(batchsize)
        if not results:
            break
        for result in results:
            yield result
```

As you can see, our function keeps yielding the results. If you used the keyword return instead of yield, then the whole function would be ended once it reached return.

return - returns only once
yield - returns multiple times
If a function uses the keyword yield then it's a generator.

Now you can iterate like this:

```python
db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="domains")
cursor = db.cursor()
cursor.execute("SELECT domain FROM domains")
for result in ResultGenerator(cursor):
    doSomethingWith(result)
db.close()
```
