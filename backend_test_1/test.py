import database as db
import random, string

db.create()
db.create_ip()

num = 160841118548804530373144878941217683565507627849937568477080008249078663536430639517370769026408664610881438552287365658774223652089417377109654663859855339256617667593601503725659239244125973452968420879286200333179621860325708390774304398641795584147801970422601641096366250131762872780592743452419319349323

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

min = int("1"+"0"*200)
max = int("9"*201)

print(min, max)
print(random.randint(min, max))


for i in range(1000000):
	print(i)
	sql = f"INSERT INTO users(id, user_name, public_key, info) VALUES({i+1}, '{get_random_string(16)}', {random.randint(min, max)}, '{get_random_string(255)}');"
	print(sql)
	db.querry(sql, "db.db")
