# GIT SETUP GUIDE

This guide will help you commit the Bitbucket DevOps CI/CD project to your git repository.

## Prerequisites
- Git installed on your system
- Access to Bitbucket account
- SSH or HTTPS credentials configured

## Step 1: Configure Git User

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

Or for this project only:
```bash
git config user.name "Your Name"
git config user.email "your.email@example.com"
```

## Step 2: Create Bitbucket Repository

1. Go to https://bitbucket.org/dashboard/repositories
2. Click "Create repository"
3. Name: `bitbucket-cicd-project`
4. Choose Private or Public
5. Click "Create repository"

## Step 3: Add Remote and Push

### Option A: HTTPS
```bash
git remote add origin https://bitbucket.org/YOUR_USERNAME/bitbucket-cicd-project.git
git branch -M main
git push -u origin main
```

### Option B: SSH
```bash
git remote add origin git@bitbucket.org:YOUR_USERNAME/bitbucket-cicd-project.git
git branch -M main
git push -u origin main
```

## Step 4: Make Initial Commit

```bash
# Add all files
git add .

# Commit with message
git commit -m "Initial commit: Bitbucket DevOps CI/CD project

- Comprehensive testing framework (unit + integration)
- Flask REST API with user management
- Bitbucket Pipelines CI/CD configuration
- Docker containerization (multi-stage build)
- Code quality checks (flake8, black, pylint)
- Test coverage reporting
- Documentation on DevOps testing trends"

# Push to remote
git push -u origin main
```

## Step 5: Create Branches

```bash
# Create develop branch
git checkout -b develop
git push -u origin develop

# Create feature branch for future development
git checkout -b feature/enhancements
git push -u origin feature/enhancements
```

## Step 6: Enable Bitbucket Pipelines

1. Go to your Bitbucket repository
2. Click Settings → Pipelines → Settings
3. Toggle "Enable Pipelines" to ON
4. Go to Pipelines → Configuration
5. Verify `bitbucket-pipelines.yml` is detected

## Step 7: Verify Repository

Visit: `https://bitbucket.org/YOUR_USERNAME/bitbucket-cicd-project`

You should see:
- All project files
- Commit history
- Pipeline configuration

## Troubleshooting

### Error: "permission denied"
**Solution**: Generate SSH key and add to Bitbucket settings
```bash
ssh-keygen -t rsa -b 4096 -C "your.email@example.com"
```

### Error: "could not read Username"
**Solution**: Ensure you have credentials stored
```bash
git config --global credential.helper store
```

### Pipeline not running
**Solution**: 
1. Ensure `bitbucket-pipelines.yml` is in root directory
2. Commit the file to repository
3. Go to Pipelines → Configuration and check for errors

## Next Steps

After pushing to Bitbucket:

1. **Set Branch Permissions**
   - Go to Settings → Repository Details → Branching Model
   - Set `develop` as main branch
   - Require PR reviews before merge

2. **Configure Notifications**
   - Go to Settings → Webhooks
   - Add notification integrations (Slack, email)

3. **Enable Pipelines Deployment**
   - Go to Pipelines → Deployments
   - Configure staging environment
   - Add deployment credentials

## Useful Git Commands

```bash
# Check status
git status

# View commit history
git log --oneline -10

# Create and push a feature branch
git checkout -b feature/my-feature
git add .
git commit -m "Add my feature"
git push -u origin feature/my-feature

# View remote configuration
git remote -v

# Update from remote
git fetch origin
git pull origin main
```

## Tips

- Commit frequently with meaningful messages
- Use feature branches for new development
- Create pull requests for code review
- Keep master/main branch production-ready
- Tag releases: `git tag -a v1.0.0 -m "Version 1.0.0"`
