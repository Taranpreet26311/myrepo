from selenium import webdriver


serverUrl = "http://localhost:5555/geoserver/web/"
workspaceName = "<tobisagoodboy>"
login = "admin"
pwd = "geoserver"
driver = webdriver.Chrome(executable_path='/home/taran/Desktop/compose/geoserver/geoapi')
# Open a browser and log in to the GeoServer admin page
browser = webdriver.Chrome()
browser.get(serverUrl)
browser.find_element_by_id("admin").send_keys(login)
browser.find_element_by_id("geoserver").send_keys(pwd)s
browser.find_element_by_class_name("positive").click()

# Navigate to the new Workspace, check the Services checkboxes, and Save
browser.get(serverUrl + "bookmarkable/org.geoserver.web.data.workspace.WorkspaceEditPage?name=" + workspaceName)
for idx in range (0,4):
  chkBox =  browser.find_element_by_name("services:services:" + str(idx) + ":enabled")
  if not (chkBox.is_selected()):
    chkBox.click()
browser.find_element_by_id("id9").click()
