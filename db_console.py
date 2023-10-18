import os
import dotenv
import mongoengine as mongo
import db_function as db_fn

dotenv.load_dotenv()
mongo.connect('mongo_tes', host=os.getenv('CONNECTION'))

inp = ''
fn_dict = {
    "add_user": db_fn.fn_wrapper(db_fn.addUser, 3),
    "print_all_user": db_fn.fn_wrapper(db_fn.printAllUser, 0)
}

while True:
    inp = input("<<--mongo->> ").strip().split(" ")
    if inp[0] in ['q', 'quit', 'Quit']:
        break
    if inp[0] in fn_dict:
        fn_dict[inp[0]].exec(inp[1:])
    else:
        print('Command not found')
