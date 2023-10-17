def sort_text_files():
    with open('files/story.txt', 'w') as f:
        f.write('     ')
    text_all_files = []
    files_list = ['1.txt', '2.txt', '3.txt']
    for file in files_list:
        line_list = []
        with open('files/' + file) as f:
            for line in f:
                line_list.append(line)
            
        text_all_files.append({'count_line': len(line_list), 'text_list': line_list})
    sort_list = sorted(text_all_files, key=lambda i: i['count_line'])
    # print(sort_list)

    with open('files/story.txt', 'a') as f:
        for obj in sort_list:
            for line in obj['text_list']:
                f.write(line)
            f.write('\n')


