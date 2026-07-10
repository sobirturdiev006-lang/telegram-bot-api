from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Account


class AccountModelTestCase(TestCase):
    """Test cases for the Account model."""

    def setUp(self):
        """Create test account for use in tests."""
        self.account = Account.objects.create(
            first_name='John',
            last_name='Doe',
            telegram_id='123456789',
            username='johndoe',
            phone_number='+998901234567'
        )

    def test_account_creation(self):
        """Test that an account can be created successfully."""
        self.assertEqual(self.account.telegram_id, '123456789')
        self.assertEqual(self.account.first_name, 'John')

    def test_full_name_property(self):
        """Test full_name property returns correct concatenated name."""
        self.assertEqual(self.account.full_name, 'John Doe')

    def test_full_name_with_null_values(self):
        """Test full_name handles null values gracefully."""
        account = Account.objects.create(telegram_id='987654321')
        self.assertEqual(account.full_name, 'Unknown User')

    def test_str_representation(self):
        """Test string representation of account."""
        self.assertEqual(str(self.account), 'John Doe')

    def test_unique_telegram_id(self):
        """Test that telegram_id must be unique."""
        with self.assertRaises(Exception):
            Account.objects.create(
                first_name='Jane',
                telegram_id='123456789'  # Duplicate
            )


class AccountStartViewTestCase(TestCase):
    """Test cases for the AccountStartView API endpoint."""

    def setUp(self):
        """Initialize API client for tests."""
        self.client = APIClient()
        self.url = '/api/start/'

    def test_create_account_success(self):
        """Test successful account creation via API."""
        data = {
            'first_name': 'Alice',
            'last_name': 'Smith',
            'telegram_id': '111111111',
            'username': 'alice'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['status'], 'success')

    def test_create_account_duplicate_telegram_id(self):
        """Test that duplicate telegram_id returns validation error."""
        Account.objects.create(
            first_name='Bob',
            telegram_id='222222222'
        )

        data = {
            'first_name': 'Bob',
            'telegram_id': '222222222',  # Duplicate
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['status'], 'error')

    def test_create_account_missing_required_field(self):
        """Test that missing telegram_id raises validation error."""
        data = {
            'first_name': 'Charlie',
            'last_name': 'Brown',
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_account_with_minimal_data(self):
        """Test account creation with only required fields."""
        data = {
            'telegram_id': '333333333'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class AccountListViewTestCase(TestCase):
    """Test cases for the AccountListView API endpoint."""

    def setUp(self):
        """Create test data."""
        self.client = APIClient()
        self.url = '/api/accounts/'

        # Create multiple test accounts
        for i in range(3):
            Account.objects.create(
                first_name=f'User{i}',
                telegram_id=f'{i}0000000',
                username=f'user{i}'
            )

    def test_list_accounts(self):
        """Test fetching list of all accounts."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Should return paginated results (default page size is 10)
        self.assertIn('results', response.data)

    def test_list_accounts_count(self):
        """Test that correct number of accounts are returned."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 3)

    def test_list_accounts_fields(self):
        """Test that all required fields are present in response."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        account = response.data['results'][0]
        required_fields = ['id', 'first_name', 'telegram_id', 'username']
        for field in required_fields:
            self.assertIn(field, account)

