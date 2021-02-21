from flask import Flask, render_template, request, redirect, url_for, send_from_directory, Response
import flask


app = flask.Flask(__name__)

@app.route('/images')
def send_image():
    f = open('../images/image.png', 'rb')
    image = f.read()
    return Response(response=image, content_type='image/png')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5555)