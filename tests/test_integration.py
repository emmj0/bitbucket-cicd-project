"""
Integration tests for API endpoints.
"""

import json
import pytest


class TestHealthEndpoint:
    """Tests for health check endpoint."""
    
    def test_health_check(self, client):
        """Test health check endpoint."""
        response = client.get('/health')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['status'] == 'healthy'
        assert 'version' in data


class TestUserEndpoints:
    """Tests for user API endpoints."""
    
    def test_create_user_success(self, client):
        """Test creating a user successfully."""
        response = client.post('/api/users',
                             json={'name': 'John Doe', 'email': 'john@example.com'},
                             content_type='application/json')
        assert response.status_code == 201
        data = json.loads(response.data)
        assert data['name'] == 'John Doe'
        assert data['email'] == 'john@example.com'
        assert 'id' in data
    
    def test_create_user_missing_name(self, client):
        """Test creating user without name."""
        response = client.post('/api/users',
                             json={'email': 'john@example.com'},
                             content_type='application/json')
        assert response.status_code == 400
        data = json.loads(response.data)
        assert 'error' in data
    
    def test_create_user_invalid_email(self, client):
        """Test creating user with invalid email."""
        response = client.post('/api/users',
                             json={'name': 'John Doe', 'email': 'invalid-email'},
                             content_type='application/json')
        assert response.status_code == 400
        data = json.loads(response.data)
        assert 'error' in data
    
    def test_create_user_invalid_json(self, client):
        """Test creating user with invalid JSON."""
        response = client.post('/api/users',
                             data='invalid json',
                             content_type='application/json')
        assert response.status_code == 400
    
    def test_get_user(self, client):
        """Test retrieving a user."""
        # Create user
        create_response = client.post('/api/users',
                                     json={'name': 'Jane Doe', 'email': 'jane@example.com'},
                                     content_type='application/json')
        user_id = json.loads(create_response.data)['id']
        
        # Get user
        get_response = client.get(f'/api/users/{user_id}')
        assert get_response.status_code == 200
        data = json.loads(get_response.data)
        assert data['name'] == 'Jane Doe'
        assert data['email'] == 'jane@example.com'
    
    def test_get_nonexistent_user(self, client):
        """Test retrieving non-existent user."""
        response = client.get('/api/users/999')
        assert response.status_code == 404
        data = json.loads(response.data)
        assert 'error' in data
    
    def test_list_users_empty(self, client):
        """Test listing users when none exist."""
        response = client.get('/api/users')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data == []
    
    def test_list_users(self, client):
        """Test listing multiple users."""
        # Create users
        client.post('/api/users',
                   json={'name': 'User 1', 'email': 'user1@example.com'},
                   content_type='application/json')
        client.post('/api/users',
                   json={'name': 'User 2', 'email': 'user2@example.com'},
                   content_type='application/json')
        
        # List users
        response = client.get('/api/users')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert len(data) == 2
        assert data[0]['name'] == 'User 1'
        assert data[1]['name'] == 'User 2'
    
    def test_404_endpoint(self, client):
        """Test 404 error handling."""
        response = client.get('/nonexistent-endpoint')
        assert response.status_code == 404
        data = json.loads(response.data)
        assert 'error' in data


class TestIntegrationFlow:
    """Integration tests for complete workflows."""
    
    def test_complete_user_workflow(self, client):
        """Test complete user creation and retrieval workflow."""
        # 1. Check health
        health_response = client.get('/health')
        assert health_response.status_code == 200
        
        # 2. Create user
        create_response = client.post('/api/users',
                                     json={'name': 'Complete Test', 'email': 'test@example.com'},
                                     content_type='application/json')
        assert create_response.status_code == 201
        user_id = json.loads(create_response.data)['id']
        
        # 3. Retrieve user
        get_response = client.get(f'/api/users/{user_id}')
        assert get_response.status_code == 200
        
        # 4. List users
        list_response = client.get('/api/users')
        assert list_response.status_code == 200
        users = json.loads(list_response.data)
        assert len(users) == 1
        assert users[0]['name'] == 'Complete Test'
