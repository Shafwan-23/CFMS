from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mysqldb import MySQL
import MySQLdb.cursors
import uuid
import config

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# MySQL configurations
app.config['MYSQL_HOST'] = config.MYSQL_HOST
app.config['MYSQL_USER'] = config.MYSQL_USER
app.config['MYSQL_PASSWORD'] = config.MYSQL_PASSWORD
app.config['MYSQL_DB'] = config.MYSQL_DB

mysql = MySQL(app)

# Home route
@app.route('/')
def home():
    return render_template('login.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        role = request.form['role']
        
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE email = %s AND password = %s AND role = %s', (email, password, role))
        
        user = cursor.fetchone()
        cursor.close()
        if user:
            session['loggedin'] = True
            session['id'] = user['id']
            session['role'] = user['role']
            if user['role'] == 'admin':
                return redirect(url_for('admin_dashboard'))
            elif user['role'] == 'student':
                return redirect(url_for('student_dashboard'))
            elif user['role'] == 'maintenance':
                return redirect(url_for('maintenance_dashboard'))
        else:
            flash('Invalid credentials!')
    return render_template('login.html')

# Register route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        role = request.form['role']
        
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO users (id, name, email, password, role) VALUES (%s, %s, %s, %s, %s)', 
                      (str(uuid.uuid4()), name, email, password, role))
        mysql.connection.commit()
        cursor.close()
        flash('Registration successful! Please login.')
        return redirect(url_for('login'))
    return render_template('register.html')

# Admin Dashboard
@app.route('/admin/dashboard')
def admin_dashboard():
    if 'loggedin' in session and session['role'] == 'admin':
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT COUNT(*) AS users FROM users')
        user_count = cursor.fetchone()['users']
        cursor.execute('SELECT COUNT(*) AS facilities FROM facilities')
        facility_count = cursor.fetchone()['facilities']
        cursor.execute('SELECT COUNT(*) AS requests FROM maintenance_requests WHERE status = "pending"')
        request_count = cursor.fetchone()['requests']
        cursor.close()
        return render_template('admin/dashboard.html', user_count=user_count, facility_count=facility_count, request_count=request_count)
    return redirect(url_for('login'))

# Admin: Manage Users
@app.route('/admin/users', methods=['GET', 'POST'])
def manage_users():
    if 'loggedin' in session and session['role'] == 'admin':
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        if request.method == 'POST':
            if 'add' in request.form:
                name = request.form['name']
                email = request.form['email']
                password = request.form['password']
                role = request.form['role']
                cursor.execute('INSERT INTO users (id, name, email, password, role) VALUES (%s, %s, %s, %s, %s)', 
                              (str(uuid.uuid4()), name, email, password, role))
                mysql.connection.commit()
                flash('User added successfully!')
            elif 'delete' in request.form:
                user_id = request.form['user_id']
                cursor.execute('DELETE FROM users WHERE id = %s', (user_id,))
                mysql.connection.commit()
                flash('User deleted successfully!')
            elif 'update' in request.form:
                user_id = request.form['user_id']
                name = request.form['name']
                email = request.form['email']
                role = request.form['role']
                cursor.execute('UPDATE users SET name = %s, email = %s, role = %s WHERE id = %s', (name, email, role, user_id))
                mysql.connection.commit()
                flash('User updated successfully!')
        cursor.execute('SELECT * FROM users')
        users = cursor.fetchall()
        cursor.close()
        return render_template('admin/manage_users.html', users=users)
    return redirect(url_for('login'))

# Admin: Manage Facilities
@app.route('/admin/facilities', methods=['GET', 'POST'])
def manage_facilities():
    if 'loggedin' in session and session['role'] == 'admin':
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        if request.method == 'POST':
            if 'add' in request.form:
                name = request.form['name']
                type = request.form['type']
                cursor.execute('INSERT INTO facilities (id, name, type) VALUES (%s, %s, %s)', 
                              (str(uuid.uuid4()), name, type))
                mysql.connection.commit()
                flash('Facility added successfully!')
            elif 'delete' in request.form:
                facility_id = request.form['facility_id']
                cursor.execute('DELETE FROM facilities WHERE id = %s', (facility_id,))
                mysql.connection.commit()
                flash('Facility deleted successfully!')
        cursor.execute('SELECT * FROM facilities')
        facilities = cursor.fetchall()
        cursor.close()
        return render_template('admin/manage_facilities.html', facilities=facilities)
    return redirect(url_for('login'))

# Admin: Manage Maintenance Requests
@app.route('/admin/maintenance', methods=['GET', 'POST'])
def manage_maintenance():
    if 'loggedin' in session and session['role'] == 'admin':
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        if request.method == 'POST':
            request_id = request.form['request_id']
            status = request.form['status']
            assigned_to = request.form['assigned_to']
            cursor.execute('UPDATE maintenance_requests SET status = %s, assigned_to = %s WHERE id = %s', 
                          (status, assigned_to, request_id))
            mysql.connection.commit()
            flash('Maintenance request updated!')
        cursor.execute('SELECT mr.*, u.name AS user_name FROM maintenance_requests mr JOIN users u ON mr.user_id = u.id')
        requests = cursor.fetchall()
        cursor.execute('SELECT * FROM users WHERE role = "maintenance"')
        maintenance_staff = cursor.fetchall()
        cursor.close()
        return render_template('admin/manage_maintenance.html', requests=requests, maintenance_staff=maintenance_staff)
    return redirect(url_for('login'))

# Admin: Manage Assets
@app.route('/admin/assets', methods=['GET', 'POST'])
def manage_assets():
    if 'loggedin' in session and session['role'] == 'admin':
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        if request.method == 'POST':
            if 'add' in request.form:
                name = request.form['name']
                type = request.form['type']
                cursor.execute('INSERT INTO assets (id, name, type) VALUES (%s, %s, %s)', 
                              (str(uuid.uuid4()), name, type))
                mysql.connection.commit()
                flash('Asset added successfully!')
            elif 'delete' in request.form:
                asset_id = request.form['asset_id']
                cursor.execute('DELETE FROM assets WHERE id = %s', (asset_id,))
                mysql.connection.commit()
                flash('Asset deleted successfully!')
        cursor.execute('SELECT * FROM assets')
        assets = cursor.fetchall()
        cursor.close()
        return render_template('admin/manage_assets.html', assets=assets)
    return redirect(url_for('login'))

# Admin: Reports
@app.route('/admin/reports')
def reports():
    if 'loggedin' in session and session['role'] == 'admin':
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT f.name, COUNT(b.id) AS bookings FROM facilities f LEFT JOIN bookings b ON f.id = b.facility_id GROUP BY f.id')
        facility_usage = cursor.fetchall()
        cursor.close()
        return render_template('admin/reports.html', facility_usage=facility_usage)
    return redirect(url_for('login'))

# Admin: Announcements
@app.route('/admin/announcements', methods=['GET', 'POST'])
def announcements():
    if 'loggedin' in session and session['role'] == 'admin':
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        if request.method == 'POST':
            title = request.form['title']
            content = request.form['content']
            cursor.execute('INSERT INTO announcements (id, title, content) VALUES (%s, %s, %s)', 
                          (str(uuid.uuid4()), title, content))
            mysql.connection.commit()
            flash('Announcement posted!')
        cursor.execute('SELECT * FROM announcements')
        announcements = cursor.fetchall()
        cursor.close()
        return render_template('admin/announcements.html', announcements=announcements)
    return redirect(url_for('login'))

# Student Dashboard
@app.route('/student/dashboard')
def student_dashboard():
    if 'loggedin' in session and session['role'] == 'student':
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM facilities')
        facilities = cursor.fetchall()
        cursor.close()
        return render_template('student/dashboard.html', facilities=facilities)
    return redirect(url_for('login'))

# Student: Book Facility
@app.route('/student/book', methods=['GET', 'POST'])
def book_facility():
    if 'loggedin' in session and session['role'] == 'student':
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        if request.method == 'POST':
            facility_id = request.form['facility_id']
            booking_date = request.form['booking_date']
            cursor.execute('INSERT INTO bookings (id, user_id, facility_id, booking_date, status) VALUES (%s, %s, %s, %s, %s)', 
                          (str(uuid.uuid4()), session['id'], facility_id, booking_date, 'pending'))
            mysql.connection.commit()
            flash('Booking request submitted!')
        cursor.execute('SELECT * FROM facilities')
        facilities = cursor.fetchall()
        cursor.close()
        return render_template('student/book_facility.html', facilities=facilities)
    return redirect(url_for('login'))

# Student: Raise Maintenance Issue
@app.route('/student/raise_issue', methods=['GET', 'POST'])
def raise_issue():
    if 'loggedin' in session and session['role'] == 'student':
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        if request.method == 'POST':
            description = request.form['description']
            facility_id = request.form['facility_id']
            cursor.execute('INSERT INTO maintenance_requests (id, user_id, facility_id, description, status) VALUES (%s, %s, %s, %s, %s)', 
                          (str(uuid.uuid4()), session['id'], facility_id, description, 'pending'))
            mysql.connection.commit()
            flash('Issue raised successfully!')
        cursor.execute('SELECT * FROM facilities')
        facilities = cursor.fetchall()
        cursor.close()
        return render_template('student/raise_issue.html', facilities=facilities)
    return redirect(url_for('login'))

# Student: View Issues
@app.route('/student/view_issues')
def view_issues():
    if 'loggedin' in session and session['role'] == 'student':
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT mr.*, f.name AS facility_name FROM maintenance_requests mr JOIN facilities f ON mr.facility_id = f.id WHERE mr.user_id = %s', 
                      (session['id'],))
        issues = cursor.fetchall()
        cursor.close()
        return render_template('student/view_issues.html', issues=issues)
    return redirect(url_for('login'))

# Student: View Announcements
@app.route('/student/view_announcements')
def view_student_announcements():
    if 'loggedin' in session and session['role'] == 'student':
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM announcements')
        announcements = cursor.fetchall()
        cursor.close()
        return render_template('student/view_announcements.html', announcements=announcements)
    return redirect(url_for('login'))

# Maintenance Dashboard
@app.route('/maintenance/dashboard')
def maintenance_dashboard():
    if 'loggedin' in session and session['role'] == 'maintenance':
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT mr.*, f.name AS facility_name FROM maintenance_requests mr JOIN facilities f ON mr.facility_id = f.id WHERE mr.assigned_to = %s', 
                      (session['id'],))
        requests = cursor.fetchall()
        cursor.close()
        return render_template('maintenance/dashboard.html', requests=requests)
    return redirect(url_for('login'))

# Maintenance: View Requests
@app.route('/maintenance/requests', methods=['GET', 'POST'])
def maintenance_requests():
    if 'loggedin' in session and session['role'] == 'maintenance':
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        if request.method == 'POST':
            request_id = request.form['request_id']
            status = request.form['status']
            comment = request.form['comment']
            cursor.execute('UPDATE maintenance_requests SET status = %s, comment = %s WHERE id = %s', 
                          (status, comment, request_id))
            mysql.connection.commit()
            flash('Request updated!')
        cursor.execute('SELECT mr.*, f.name AS facility_name FROM maintenance_requests mr JOIN facilities f ON mr.facility_id = f.id WHERE mr.assigned_to = %s', 
                      (session['id'],))
        requests = cursor.fetchall()
        cursor.close()
        return render_template('maintenance/view_requests.html', requests=requests)
    return redirect(url_for('login'))

# Logout
@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('role', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)