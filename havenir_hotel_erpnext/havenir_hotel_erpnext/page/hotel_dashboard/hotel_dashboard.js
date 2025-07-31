frappe.pages['hotel-dashboard'].on_page_load = function (wrapper) {
    var page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Hotel Dashboard',
        single_column: true
    });

    // Add container for the dashboard
    $(page.body).append(`
        <div class="dashboard-container">
            <div class="row mb-4" id="summary-cards">
                <div class="col-md-4">
                    <div class="summary-card total-rooms">
                        <div class="card-body">
                            <h3 id="total-rooms-count">0</h3>
                            <p>Total Rooms</p>
                        </div>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="summary-card check-in-rooms">
                        <div class="card-body">
                            <h3 id="checked-in-rooms-count">0</h3>
                            <p>Checked-In</p>
                        </div>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="summary-card reserved-rooms">
                        <div class="card-body">
                            <h3 id="reserved-rooms-count">0</h3>
                            <p>Reserved</p>
                        </div>
                    </div>
                </div>
            </div>
			<div class="col-md-4">
                    <div class="summary-card reserved-rooms">
                        <div class="card-body">
                            <h3 id="reserved-rooms-dirty">0</h3>
                            <p>Reserved</p>
                        </div>
                    </div>
                </div>
            </div>
			<div class="col-md-4">
                    <div class="summary-card reserved-rooms">
                        <div class="card-body">
                            <h3 id="reserved-rooms-clean">0</h3>
                            <p>Reserved</p>
                        </div>
                    </div>
                </div>
            </div>
            <div class="row" id="rooms-dashboard">
                <div class="col-md-12 text-center">
                    <h2>Loading Rooms Data...</h2>
                </div>
            </div>
        </div>
    `);

    // Fetch Rooms Data
    frappe.call({
        method: 'frappe.client.get_list',
        args: {
            doctype: 'Rooms',
            fields: ['room_number', 'room_type', 'room_status', 'housekeeping_status', 'inspection_status', 'price']
        },
        callback: function (response) {
            if (response.message) {
                let rooms = response.message;
                updateSummaryCards(rooms);
                renderDashboard(rooms);
            } else {
                frappe.msgprint('No data found for Rooms');
            }
        },
        error: function (err) {
            console.error(err);
            frappe.msgprint('Failed to fetch data for Rooms');
        }
    });
};

// Update Summary Cards
function updateSummaryCards(rooms) {
    let totalRooms = rooms.length;
    let checkedInRooms = rooms.filter(room => room.room_status === 'Checked-In').length;
    let reservedRooms = rooms.filter(room => room.room_status === 'Reserved').length;
	const housekeepingDirty = rooms.filter((room) => room.housekeeping_status === 'Dirty').length;
    const housekeepingCleaned = rooms.filter((room) => room.housekeeping_status === 'Cleaned').length;


    $('#total-rooms-count').text(totalRooms);
    $('#checked-in-rooms-count').text(checkedInRooms);
    $('#reserved-rooms-count').text(reservedRooms);
	$('#reserved-rooms-dirty').text(housekeepingDirty);
	$('#reserved-rooms-clean').text(housekeepingCleaned);
}

// Function to Render Dashboard
function renderDashboard(rooms) {
    let dashboard = $('#rooms-dashboard');
    dashboard.empty(); // Clear existing content

    if (rooms.length === 0) {
        dashboard.append(`<div class="col-md-12 text-center"><h4>No Rooms Found</h4></div>`);
        return;
    }

    rooms.forEach(room => {
        let cardColor = getCardColor(room.room_status); // Dynamic card color
        dashboard.append(`
            <div class="col-md-4 mb-3">
                <div class="room-card" style="background-color: ${cardColor}; color: white; padding: 20px; border-radius: 10px;">
                    <div class="room-header">
                        <h4><i class="fa fa-bed"></i> Room ${room.room_number}</h4>
                        <p>Type: ${room.room_type}</p>
                    </div>
                    <div class="room-body">
                        <p>Status: ${room.room_status}</p>
                        <p>Housekeeping: ${room.housekeeping_status}</p>
                        <p>Inspection: ${room.inspection_status}</p>
                        <p>Price: $${room.price}</p>
                    </div>
                </div>
            </div>
        `);
    });
}

// Function to Get Card Color Based on Room Status
function getCardColor(status) {
    switch (status) {
        case 'Available':
            return '#28a745'; // Green
        case 'Checked-In':
            return '#007bff'; // Blue
        case 'Reserved':
            return '#ffc107'; // Yellow
        case 'Out of Service':
            return '#dc3545'; // Red
        default:
            return '#6c757d'; // Gray
    }
}


// Add CSS dynamically to the page
function addCustomStyles() {
    const style = document.createElement('style');
    style.type = 'text/css';
    style.innerHTML = `
        /* Summary Cards */
        .summary-card {
            background: #f8f9fa;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            text-align: center;
            padding: 20px;
            color: #343a40;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        .summary-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
        }
        
        .summary-card h3 {
            font-size: 2.5rem;
            margin-bottom: 10px;
        }
        
        .summary-card p {
            font-size: 1.2rem;
            margin: 0;
            font-weight: 500;
        }
        
        .total-rooms {
            background-color: #17a2b8;
            color: white;
        }
        
        .check-in-rooms {
            background-color: #007bff;
            color: white;
        }
        
        .reserved-rooms {
            background-color: #ffc107;
            color: white;
        }
        
        /* Room Cards */
        .room-card {
            color: white;
            padding: 20px;
            border-radius: 10px;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        
        .room-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
        }
        
        .room-header {
            font-size: 1.5rem;
            margin-bottom: 10px;
        }
        
        .room-body p {
            margin: 5px 0;
        }
    `;
    document.head.appendChild(style);
}

// Call this function when the page loads
addCustomStyles();
