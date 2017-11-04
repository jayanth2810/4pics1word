__author__ = 'jayanthvenkataraman'

from itertools import permutations
import json, os

from flask import request, Response
from flask.ext.restplus import fields, Resource

from app import api, app

RESOURCES_DIRECTORY = "resources/"
ENGLISH_WORDS_FILE_NAME = "word_list.txt"

ns = api.namespace('4 Pic 1 Word', description='',
                   path='/api/1.0')

request_field = api.model('Enter the data', {
    'character_set': fields.String(description='The Character Set that makes up the word', required=True),
    'number_of_letter': fields.Integer(description='The number of letters in the word', required=True),
})


def _get_possible_permutations(characters, number_of_letters):
    return [''.join(i) for i in permutations(characters, number_of_letters)]


def _get_valid_english_words(possible_permutations):
    path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), RESOURCES_DIRECTORY +
                                        ENGLISH_WORDS_FILE_NAME))

    try:
        with open(path) as word_file:
            english_words = set(word.strip().lower() for word in word_file)
        valid_english_words = [i for i in possible_permutations if i in english_words]
        return set(valid_english_words)
    except Exception as e:
        print("Exception is ", str(e))
        return set()


def _get_possible_words(characters, number_of_words):
    possible_permutations = _get_possible_permutations(characters, number_of_words)
    valid_english_words = _get_valid_english_words(possible_permutations)
    return valid_english_words


def set_response_and_return_result(status, message, data, status_code):
    print(status, message, data, status_code)
    result_dict = {"message": message, "status": status, "data": data}
    return result_dict, status_code


def get_list_of_possible_words(characters, number_of_letters):
    try:
        valid_answers = list(_get_possible_words(characters, number_of_letters))
        list.sort(valid_answers)
        return set_response_and_return_result("OK",
                                              ' '.join(["There are ", str(len(valid_answers)), " possible answers"]),
                                              valid_answers, 200)
    except Exception as e:
        print("Exception ", str(e))
        return set_response_and_return_result("ERROR",
                                              "Server Error. Please try later",
                                              [], 500)


@ns.route('/possible-words')
class PossibleWords(Resource):
    @api.doc(params={'character_set': 'The Character Set that makes up the word'})
    @api.doc(params={'number_of_letter': 'The number of letters in the word'})
    @api.response(200, 'Success')
    @api.response(400, 'Bad Request')
    @api.response(500, 'Internal Server Error')
    def get(self):
        if not request.args.get('character_set') or not request.args.get('number_of_letter'):
            return set_response_and_return_result("ERROR", "Insufficent Input. Enter all inputs", [], 400)
        return get_list_of_possible_words(request.args.get('character_set'), int(request.args.get('number_of_letter')))
