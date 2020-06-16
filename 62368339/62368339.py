from os import listdir

# Getting list of all image files in directory
location = 'Test/'
excluding = 'This_is_.wav', 'slience_2sec.wav'

# Fetching .wav audio clips
audios = [name for name in listdir(location) if name.endswith('.wav')]
for exclude in excluding:
    audios.remove(exclude)

print(audios)


# creating padding form
padding_list = [f"file {name}" for name in excluding]
padding_list.append(padding_list[0])  # adding first element one more time.


# Saving
for audio in audios:
    with open(location + audio + '-audio.txt', 'w') as file:
        temp = padding_list[:] + [f"file {audio}"]
        output = '\n'.join(temp)
        file.write('\n\n'.join([output, output]))
