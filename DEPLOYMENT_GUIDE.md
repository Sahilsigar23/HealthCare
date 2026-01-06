# 🚀 Deploy Healthcare Backend to Render

Complete guide to deploy your Django Healthcare Backend to Render.com

---

## 📋 Prerequisites

✅ **Already Done:**
- Django project with Neon PostgreSQL
- All code committed
- Neon database configured and seeded
- Production-ready settings

✅ **You Need:**
- GitHub account
- Render account (free)
- Neon database credentials (you have these)

---

## 🎯 Step 1: Push to GitHub

### 1. Initialize Git (if not already done)
```bash
git init
git add .
git commit -m "Initial commit: Healthcare Backend API"
```

### 2. Create GitHub Repository
1. Go to https://github.com/new
2. Repository name: `healthcare-backend-api`
3. Keep it **Public** or **Private** (your choice)
4. **Don't** add README, .gitignore, or license (we already have them)
5. Click **Create repository**

### 3. Push to GitHub
```bash
git remote add origin https://github.com/YOUR_USERNAME/healthcare-backend-api.git
git branch -M main
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username!

---

## 🌐 Step 2: Deploy on Render

### 1. Create Render Account
- Go to: https://render.com/
- Click **Get Started**
- Sign up with **GitHub** (recommended)

### 2. Create New Web Service
1. Click **New +** → **Web Service**
2. Connect your GitHub repository
3. Select **healthcare-backend-api** repository
4. Click **Connect**

### 3. Configure Service

#### Basic Settings:
- **Name:** `healthcare-backend-api` (or your choice)
- **Region:** Choose closest to you
- **Branch:** `main`
- **Root Directory:** Leave blank
- **Runtime:** `Python 3`
- **Build Command:** `./build.sh`
- **Start Command:** `gunicorn healthcare_backend.wsgi:application`

#### Instance Type:
- Select **Free** (or paid if you prefer)

### 4. Add Environment Variables

Click **Advanced** → **Add Environment Variable**

Add these variables **one by one**:

```
SECRET_KEY=your-secret-key-here-generate-new-one
DEBUG=False
ALLOWED_HOSTS=your-app-name.onrender.com
DB_NAME=neondb
DB_USER=neondb_owner
DB_PASSWORD=npg_0PNXZ4cmUDtb
DB_HOST=ep-wild-truth-ahglr2hd-pooler.c-3.us-east-1.aws.neon.tech
DB_PORT=5432
CORS_ALLOW_ALL_ORIGINS=True
```

**Important:**
- Replace `your-app-name.onrender.com` with your actual Render URL
- Use your actual Neon credentials
- Generate new SECRET_KEY: https://djecrety.ir/

### 5. Deploy!
Click **Create Web Service**

Render will:
1. Clone your repository
2. Install dependencies
3. Collect static files
4. Run migrations
5. Seed database
6. Start your app

⏳ **This takes 3-5 minutes**

---

## ✅ Step 3: Verify Deployment

### Check Build Logs
- Watch the deployment logs
- Should see: "Build successful"
- Should see: "Your service is live 🎉"

### Test Your API

**1. Visit Welcome Page:**
```
https://your-app-name.onrender.com/
```

Should show API welcome message!

**2. Test Login Endpoint:**
```bash
curl -X POST https://your-app-name.onrender.com/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"email":"rajesh.kumar@email.com","password":"Test@123"}'
```

**3. Access Admin Panel:**
```
https://your-app-name.onrender.com/admin/
```

Login: admin@healthcare.com / admin@123

---

## 📱 Step 4: Update Postman

### Update Base URL:
1. Open Postman Collection
2. Click on Collection → **Variables**
3. Change `base_url` from:
   - `http://127.0.0.1:8000`
   - To: `https://your-app-name.onrender.com`
4. Save

Now test all endpoints!

---

## 🔧 Common Issues & Solutions

### Issue 1: "Application failed to respond"
**Solution:**
- Check if `ALLOWED_HOSTS` includes your Render URL
- Check environment variables are set correctly
- View logs: Dashboard → Logs

### Issue 2: "Database connection failed"
**Solution:**
- Verify Neon database is active (not paused)
- Check all DB_* environment variables
- Ensure `sslmode=require` in settings

### Issue 3: "Static files not loading"
**Solution:**
- Already fixed with WhiteNoise
- Run: `python manage.py collectstatic`
- Check build logs

### Issue 4: "Build failed"
**Solution:**
- Check `requirements.txt` is correct
- Ensure `build.sh` has execute permissions
- Check Python version compatibility

---

## 🎨 Production Optimizations

### 1. Custom Domain (Optional)
1. Go to Settings → Custom Domains
2. Add your domain
3. Update DNS records
4. Update `ALLOWED_HOSTS`

### 2. Environment Variables Best Practices
- Never commit `.env` file
- Generate new SECRET_KEY for production
- Set `DEBUG=False` in production
- Use Render's environment variables feature

### 3. Database Backups
- Neon automatically backs up your database
- Access backups in Neon dashboard
- Can restore any point in time

### 4. Monitor Your App
- Render Dashboard → Metrics
- See CPU, Memory usage
- Monitor request logs
- Set up alerts

---

## 📊 Your Deployed URLs

After deployment, you'll have:

### API Endpoints:
```
https://your-app-name.onrender.com/
https://your-app-name.onrender.com/api/auth/register/
https://your-app-name.onrender.com/api/auth/login/
https://your-app-name.onrender.com/api/patients/
https://your-app-name.onrender.com/api/doctors/
https://your-app-name.onrender.com/api/mappings/
https://your-app-name.onrender.com/admin/
```

### Test Credentials:
- **Admin:** admin@healthcare.com / admin@123
- **User 1:** rajesh.kumar@email.com / Test@123
- **User 2:** priya.sharma@email.com / Test@123
- **User 3:** amit.patel@email.com / Test@123

---

## 🔄 Updating Your Deployment

### After making changes:
```bash
git add .
git commit -m "Your update message"
git push origin main
```

Render will **automatically redeploy** your app!

---

## 💡 Free Tier Limitations

### Render Free Tier:
- ✅ 750 hours/month (plenty for one app)
- ✅ Automatic SSL certificate
- ✅ Custom domains
- ⏸️ Spins down after 15 min inactivity
- 🐌 Cold start: ~30-60 seconds

### Neon Free Tier:
- ✅ 512 MB storage
- ✅ Unlimited API requests
- ✅ Auto-pauses after inactivity
- ✅ Auto-resumes on access

**Both are perfect for development/portfolio projects!**

---

## 🎯 Quick Checklist

Before deploying:
- [ ] Code pushed to GitHub
- [ ] `.env` not committed (in .gitignore)
- [ ] `build.sh` created
- [ ] `requirements.txt` updated with gunicorn & whitenoise
- [ ] `STATIC_ROOT` configured
- [ ] Neon database working locally

During deployment:
- [ ] Repository connected to Render
- [ ] All environment variables added
- [ ] Build command: `./build.sh`
- [ ] Start command: `gunicorn healthcare_backend.wsgi:application`

After deployment:
- [ ] Build successful
- [ ] Welcome page loads
- [ ] Login API works
- [ ] Admin panel accessible
- [ ] Postman collection updated

---

## 📚 Additional Resources

- **Render Docs:** https://render.com/docs
- **Django Deployment:** https://docs.djangoproject.com/en/5.0/howto/deployment/
- **Neon Docs:** https://neon.tech/docs
- **Gunicorn Docs:** https://docs.gunicorn.org/

---

## 🆘 Need Help?

### Check These:
1. Render deployment logs
2. Neon connection status
3. Environment variables
4. GitHub repository

### Debug Deployment:
```bash
# On Render, open Shell tab and run:
python manage.py check
python manage.py showmigrations
python manage.py test
```

---

**Your healthcare backend will be live at:**
**`https://your-app-name.onrender.com`** 🎉

Share this URL to showcase your API!
