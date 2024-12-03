singers = {x for x in input("Enter names of singers separated by space: ").split()}
dancers = {x for x in input("Enter names of dancers separated by space: ").split()}
all_artists = singers | dancers
all_rounders = singers & dancers
dancers_not_singers = dancers - singers
singers_not_dancers = singers - dancers
dancers_xor_singers = dancers ^ singers
print(f"All artists of the class: {all_artists}")
print(f"All-rounders of the class: {all_rounders}")
print(f"Dancers but not singers: {dancers_not_singers}")
print(f"Singers but not dancers: {singers_not_dancers}")
print(f"Dancers but not singers cum singers but not dancers: {dancers_xor_singers}")