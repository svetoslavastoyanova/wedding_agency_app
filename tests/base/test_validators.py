from unittest import TestCase

from django.core.exceptions import ValidationError

from djangoProject.core.validators import first_letter_validator, last_name_validator, age_validator, first_name_validator


class ValidateFirstNameTest(TestCase):
    def test_validatorRaisesException(self):
        with self.assertRaises(ValidationError):
            first_name_validator('svetoslava')

    def test_validatorPassesTest(self):
        result = first_name_validator('Svetoslava')
        self.assertEqual(result, 'Svetoslava')


class ValidateLastNameTest(TestCase):
    def test_validatorRaisesException(self):
        with self.assertRaises(ValidationError):
            last_name_validator('svetoslava')

    def test_validatorPassesTest(self):
        result = last_name_validator('Svetoslava')
        self.assertEqual(result, 'Svetoslava')


class ValidateAgeTest(TestCase):
    def test_AgeValidatorRaisesException(self):
        with self.assertRaises(ValidationError):
            age_validator(-10)

    def test_AgeValidatorPassesTest(self):
        result = age_validator(10)
        self.assertIsNone(result)


class ValidateFirstLetterTest(TestCase):
    def test_validatorRaisesException(self):
        with self.assertRaises(ValidationError):
            first_letter_validator('abv')

    def test_validatorPassesTest(self):
        result = first_letter_validator('Abv')
        self.assertEqual(result, 'Abv')



