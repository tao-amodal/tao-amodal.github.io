import os

if __name__ == '__main__':
    dir_path = './static/dataset_videos'
    num_files = 0


    with open('./dataset.html', 'w') as f:
        f.write('<!DOCTYPE html>\n')
        f.write('<html>\n')
        f.write('<body style="text-align: center;"> \n\n')
        f.write('\t<div class="columns is-centered has-text-centered">\n'
                '\t\t<h1>TAO-Amodal - Ramdomly selected examples</h1>\n'
                '\t</div>\n'
                '\t<div class="columns is-centered has-text-centered">\n'
                '\t\t<div class="publication-links">\n'
                '\t\t\t<span class="link-block">\n'
                '\t\t\t\t<a href="index.html" class="external-link button is-normal is-rounded is-dark">\n'
                '\t\t\t\t\t<span class="icon">\n'
                '\t\t\t\t\t\t<i class="fas fa-database"></i>\n'
                '\t\t\t\t\t</span>\n'
                '\t\t\t\t\t<span>Homepage</span>\n'
                '\t\t\t\t</a>\n'
                '\t\t\t</span>\n'
                '\t\t</div>\n'
                '\t</div>\n'
            )
        for root, dirs, files in os.walk(dir_path, topdown=False):
            for name in files:
                num_files += 1
                video_path = os.path.join(root, name)
                f.write('\n\t<video height="700" autoplay muted loop>\n\n')
                f.write('\t\t<source src="{}"'.format(video_path))
                f.write(' type="video/mp4">\n')
                f.write('\t</video>\n')
        f.write('</body>\n')
        f.write('</html> ')

    print("Writing {} files into dataset.html...".format(num_files))