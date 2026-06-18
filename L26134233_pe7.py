# Analyze forum replies and print the required result

# This recursive function visits all comments under one post
def visit_comments(post_id, comments, depth, flat_list, author_likes):
    total = 0

    # Go through every comment in this level
    for comment_id in comments:
        comment = comments[comment_id]

        likes = comment["likes"]
        author = comment["author"]

        # Add likes to this post's total
        total = total + likes

        # Add this comment to flattened list
        flat_list.append((post_id, comment_id, depth, likes))

        # Add likes to this author's total
        if author not in author_likes:
            author_likes[author] = 0
        author_likes[author] = author_likes[author] + likes

        # Visit replies recursively
        replies = comment["replies"]
        reply_total = visit_comments(post_id, replies, depth + 1, flat_list, author_likes)

        # Add replies' likes to total
        total = total + reply_total

    return total


# This function prints the result in the required format
def print_result(result):
    print("{")

    # Print total_likes
    print("    'total_likes': {")
    for post_id in result["total_likes"]:
        print("        " + str(post_id) + ": " + str(result["total_likes"][post_id]) + ",")
    print("    },")

    # Print max_likes_post
    print("    'max_likes_post': " + str(result["max_likes_post"]) + ",")

    # Print flattened
    print("    'flattened': [")
    for item in result["flattened"]:
        print("        " + str(item) + ",")
    print("    ],")

    # Print author_likes
    print("    'author_likes': {")
    for author in result["author_likes"]:
        print("        '" + author + "': " + str(result["author_likes"][author]) + ",")
    print("    }")

    print("}")


# This function analyzes the whole forum
def analyze_forum(forum):
    total_likes = {}
    flattened = []
    author_likes = {}

    # Analyze each post
    for post_id in forum:
        comments = forum[post_id]["comments"]

        post_total = visit_comments(post_id, comments, 1, flattened, author_likes)
        total_likes[post_id] = post_total

    # Find the post with maximum total likes
    max_likes_post = None
    max_likes = -1

    for post_id in total_likes:
        if total_likes[post_id] > max_likes:
            max_likes = total_likes[post_id]
            max_likes_post = post_id

    # Create the final output dictionary
    result = {
        "total_likes": total_likes,
        "max_likes_post": max_likes_post,
        "flattened": flattened,
        "author_likes": author_likes
    }

    # Print the final result
    print_result(result)


# Main program
forum = {}

f = open("forum1.txt", "r")
code = f.read()
f.close()

# Execute the file content to create the forum dictionary
exec(code)

analyze_forum(forum)