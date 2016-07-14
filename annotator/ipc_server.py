import json

import ipc
import deploy


def server_process_request(image_path):
    try:
        # note that we have to explicitly pass the params to predict function
        annotation = deploy.predict(image_path, vgg, ria, dictionary)
    except KeyError:
        annotation = []
    return annotation 


if __name__ == '__main__':
    server_address = ('localhost', 5795)

    print 'Start loading models and dictionary, please wait for about 10 seconds'
    vgg, ria = deploy.load_models();

    with open('dictionary.json') as f:
        dictionary = json.load(f)

    print 'Model Loading completed'
    print 'Ready for annotating'

    ipc.Server(server_address, server_process_request).serve_forever()
