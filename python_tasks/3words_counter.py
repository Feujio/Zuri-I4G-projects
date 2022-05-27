text = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Officia nobis obcaecati quae dicta, maiores cumque sed voluptatibus, ducimus nostrum accusantium corrupti illo quibusdam! Pariatur, a vitae aliquam eos ipsam libero."

def words_counter(text):
    return len(text.split())

print( f"The given text contains: {words_counter(text)} words.")
