# define a class to get attributes from drone using dronekit-python
class drone_state(object):
	# initialize the class
	def __init__(self):
		# connect to the drone
		self.vehicle = connect('/dev/ttyACM0', wait_ready=True)
		# define the data to be returned
		self.lat = self.vehicle.location.global_frame.lat
		self.lon = self.vehicle.location.global_frame.lon
		self.alt = self.vehicle.location.global_frame.alt
		self.vel = self.vehicle.velocity
		self.head = self.vehicle.heading
		self.pitch = self.vehicle.attitude.pitch
		self.roll = self.vehicle.attitude.roll
		self.yaw = self.vehicle.attitude.yaw
		self.vehicle.close()
		# define a function to return all the data
		def get_state(self):
			return self.__dict__.values()

# class to get the image from the drone
class drone_image(object):
	# initialize the class
	def __init__(self):
		# connect to the drone
		self.vehicle = connect('/dev/ttyACM0', wait_ready=True)
		# create a new camera object
		camera = Camera(self.vehicle)
		# start the camera
		camera.start_capture()
		# sleep for 1 second to let it initialize
		time.sleep(1)
		# define the data to be returned
		def get_image(self):
			# get the image from the camera
			img = camera.capture(encoding='jpeg')
			# close the camera
			camera.close()
			# return the image
			return img

# define a class to get the battery level from the drone
class drone_battery(object):
	# initialize the class
	def __init__(self):
		# connect to the drone
		self.vehicle = connect('/dev/ttyACM0', wait_ready=True)
		# define the data to be returned
		self.level = self.vehicle.battery.level
		self.vehicle.close()
		# define a function to return all the data
		def get_state(self):
			return self.__dict__.values()

# define a class to get the gps coordinates from the drone
class drone_gps(object):
	# initialize the class
	def __init__(self):
		# connect to the drone
		self.vehicle = connect('/dev/ttyACM0', wait_ready=True)
		# define the data to be returned
		self.lat = self.vehicle.location.global_frame.lat
		self.lon = self.vehicle.location.global_frame.lon
		self.vehicle.close()
		# define a function to return all the data
		def get_state(self):
			return self.__dict__.values()

# define a class to get the current heading from the drone
class drone_heading(object):
	# initialize the class
	def __init__(self):
		# connect to the drone
		self.vehicle = connect('/dev/ttyACM0', wait_ready=True)
		# define the data to be returned
		self.head = self.vehicle.heading
		self.vehicle.close()
		# define a function to return all the data
		def get_state(self):
			return self.__dict__.values()

# define a class to get the current altitude from the drone
class drone_altitude(object):
	# initialize the class
	def __init__(self):
		# connect to the drone
		self.vehicle = connect('/dev/ttyACM0', wait_ready=True)
		# define the data to be returned
		self.alt = self.vehicle.location.global_frame.alt
		self.vehicle.close()
		# define a function to return all the data
		def get_state(self):
			return self.__dict__.values()

# define a class to get the current velocity from the drone
class drone_velocity(object):
	# initialize the class
	def __init__(self):
		# connect to the drone
		self.vehicle = connect('/dev/ttyACM0', wait_ready=True)
		# define the data to be returned
		self.vel = self.vehicle.velocity
		self.vehicle.close()
		# define a function to return all the data
		def get_state(self):
			return self.__dict__.values()

# define a function to fly to a specified GPS coordinate
def fly_to_coordinate(lat, lon, alt):
	# connect to the drone
	vehicle = connect('/dev/ttyACM0', wait_ready=True)
	# print the current location
	print "Current location: %s" % vehicle.location.global_frame
	# define the target location
	targetLocation = LocationGlobalRelative(lat, lon, alt)
	# print the target location
	print "Target location: %s" % targetLocation
	# fly to the target location
	vehicle.simple_goto(targetLocation)
	# close the vehicle connection
	vehicle.close()

# define a function to take off to a specified altitude
def take_off(altitude):
	# connect to the drone
	vehicle = connect('/dev/ttyACM0', wait_ready=True)
	# print the current location
	print "Current location: %s" % vehicle.location.global_frame
	# take off to the specified altitude
	vehicle.simple_takeoff(altitude)
	# close the vehicle connection
	vehicle.close()

# define a function to land the drone
def land():
	# connect to the drone
	vehicle = connect('/dev/ttyACM0', wait_ready=True)
	# print the current location
	print "Current location: %s" % vehicle.location.global_frame
	# land the drone
	vehicle.mode = VehicleMode("LAND")
	# close the vehicle connection
	vehicle.close()

# define a function to take a photo
def take_photo():
	# connect to the drone
	vehicle = connect('/dev/ttyACM0', wait_ready=True)
	# create a new camera object
	camera = Camera(vehicle)
	# start the camera
	camera.start_capture()
	# sleep for 1 second to let it initialize
	time.sleep(1)
	# get the image from the camera
	img = camera.capture(encoding='jpeg')
	# close the camera
	camera.close()
	# save the image
	f = open('image.jpg', 'w')
	f.write(img)
	f.close()
	# close the vehicle connection
	vehicle.close()

# define a function to return the current location
def get_location():
	# connect to the drone
	vehicle = connect('/dev/ttyACM0', wait_ready=True)
	# define the data to be returned
	lat = vehicle.location.global_frame.lat
	lon = vehicle.location.global_frame.lon
	# close the vehicle connection
	vehicle.close()
	# return the data
	return lat, lon

# define a function to return the current battery level
def get_battery():
	# connect to the drone
	vehicle = connect('/dev/ttyACM0', wait_ready=True)
	# define the data to be returned
	level = vehicle.battery.level
	# close the vehicle connection
	vehicle.close()
	# return the data
	return level

# define a function to return the current GPS coordinates
def get_gps():
	# connect to the drone
	vehicle = connect('/dev/ttyACM0', wait_ready=True)
	# define the data to be returned
	lat = vehicle.location.global_frame.lat
	lon = vehicle.location.global_frame.lon
	# close the vehicle connection
	vehicle.close()
	# return the data
	return lat, lon

# define a function to return the current heading
def get_heading():
	# connect to the drone
	vehicle = connect('/dev/ttyACM0', wait_ready=True)
	# define the data to be returned
	head = vehicle.heading
	# close the vehicle connection
	vehicle.close()
	# return the data
	return head

# define a function to return the current altitude
def get_altitude():
	# connect to the drone
	vehicle = connect('/dev/ttyACM0', wait_ready=True)
	# define the data to be returned
	alt = vehicle.location.global_frame.alt
	# close the vehicle connection
	vehicle.close()
	# return the data
	return alt

# define a function to return the current velocity
def get_velocity():
	# connect to the drone
	vehicle = connect('/dev/ttyACM0', wait_ready=True)
	# define the data to be returned
	vel = vehicle.velocity
	# close the vehicle connection
	vehicle.close()
	# return the data
	return vel