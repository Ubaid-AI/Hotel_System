## Havenir Hotel Erpnext

Hotel Management App for ERPNext

### Getting started

1. **Set up Frappe/ERPNext**
   ```bash
   # install bench
   pip install frappe-bench
   bench init frappe-bench && cd frappe-bench
   bench new-site hotel.local
   bench get-app https://github.com/your-user/Hotel_System.git
   bench --site hotel.local install-app havenir_hotel_erpnext
   bench start
   ```

2. **Run the Vue frontend**
   ```bash
   cd Hotel_System/frontend
   npm install
   npm run dev
   ```
   The development server proxies `/api` requests to your running Frappe
   backend at `http://localhost:8000`.

3. Open the browser at `http://localhost:5173` to view the modern UI that lists
   available rooms.

#### License

MIT
