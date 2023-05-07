from tkinter import *
from tkinter import messagebox
import ast
import winsound

#Let me create the  main window. 
main_window=Tk()

#setting the title of the Application. 
main_window.title("Co-fiver (version 1.0.0)")

#setting the dimesnion of the Application 
main_window.geometry('800x500+30+30')

#lets add a backround color
main_window.configure(bg='#fff')

#we do not want any user to  modify the size of the screen
main_window.resizable(False,False)

##let us add an image to the application.
my_image=PhotoImage(file='kafelo.png')

##so where do we place that image at???
Label(main_window,image=my_image,width=300,height=300,bg='white').place(x=10,y=10)


##lets create an area for the logginsg and loggouts!!
Area=Frame(main_window,width=500,height=300,bg='white')

##within our window, where specifically are we going to have this login area.
Area.place(x=350,y=10)


#so  lets give  our Frame an heading
heading=Label(Area,text="Login",bg='white',fg="#57a1f8",font=('microsoft Yahei UI',23,'bold'))
heading.place(x=100,y=10)




##lets add a text before the username entry  field.
username_label=Label(Area,text="username/email",bg="white")
username_label.place(x=10,y=65)
#lets now create the place where we will have  our user key in their username and their password as well. 
username_entrypoint=Entry(Area,width=40,fg='black',bg="#F0EAD6",border=0)
username_entrypoint.place(x=10,y=95)





##lets add a text before the password  entry  field.
username_label=Label(Area,text="password",bg="white")
username_label.place(x=10,y=135)

#lets now create the place where teh user will enter their login password.
password_entrypoint=Entry(Area,width=40,fg='black',bg="#F0EAD6",border=0)
password_entrypoint.place(x=10,y=165)


#import the necessary packages required for automation.
import undetected_chromedriver as uc 
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pygame
pygame.init()

 

def automate():
    options = Options()
    url = "https://www.sweetstudy.com/student-auth-wizard?authOption=sign-in"
    driver = uc.Chrome(options=options)
    driver.get(url)
    time.sleep(5)

    #lets store  the username and password
    username=username_entrypoint.get()
    password=password_entrypoint.get()

    #Lets login to the sweetstudy website and Apply for Jobs. 
    try:
        driver.find_element(By.NAME, "forms.user.password").send_keys(password)
        driver.find_element(By.NAME, "forms.user.username").send_keys(username)
        driver.find_element(By.XPATH, "//*[@id=\"wrapper\"]/div[2]/main/form/button").click()
    except:
        winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
        messagebox.showinfo("Failed!", "Restart Co-fiver kindly")
        driver.close()

    ##after this point i want to customise a text ("Successfully  logged in!")


    time.sleep(5)
    job_market= driver.find_elements(By.CSS_SELECTOR, ".css-1xxbh89")
    jobs_available_now=len(job_market)
    if jobs_available_now!=6:
        while jobs_available_now!=6:
            try:
                time.sleep(5)
                driver.refresh()
                time.sleep(5)
                newr = driver.find_elements(By.CSS_SELECTOR, ".css-1xxbh89")
                ava= len(newr)
                if ava >0:
                    break
                else:
                    continue
            except:
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                messagebox.showinfo("Co-Fiver Error", "Unable to  find jobs after successfully logged-in")
                driver.close()
    else:
        pass
    
    #Lets confirm if we have logged in successfully and found The list of  jobs Available.
    try:
        #old jobs:
        old_jobs_list=[]
        old_jobs = driver.find_elements(By.CSS_SELECTOR, ".css-1xxbh89")
        for old in old_jobs:
            old_jobs_list.append(old.text)
    

        available = len(old_jobs)
        My_Client_Budget=[]
        My_Bid_Amount=[]
        Assigment_Category=[]
        My_Bid_Position=[]
        job_posting_date=[]
        time_job_posted=[]
        client_captive_instruction=[]
        job_field=[]
        print("Your have logged in succesfully and ",available,"jobs available so far")
    except:
        print("An Error Occurred while trying to login and webscrape the jobs available")
        winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
        messagebox.showinfo("Error", "please Restart Co-Fiver ")
        driver.close()
    for i in range(available):
        jobs = driver.find_elements(By.CSS_SELECTOR, ".css-1xxbh89")
    
        #open a single job and bid for the Job. 
        job = jobs[i]
        attempt=0
        max_attempt=10
        while attempt< max_attempt:
            try:
                job.click()
                break
            except:
                print("unable to access the click button in attempt",attempt,"but i will keep on trying")
                attempt+=1
                time.sleep(7)
        time.sleep(5)
        #If the Bidding to a particular Job has not been done, let our bot bid for the job. 
        try:
            Bid_Button=driver.find_element(By.XPATH, "//*[@id=\"main-question\"]/button")
            #Before Anything, lets first get  the clients Budget:
            p=driver.find_element(By.CSS_SELECTOR, ".css-y8sxh5:nth-child(3)")
            my_p=p.text
            My_Client_Budget.append(my_p)

            
            #Lets get the date in which a particular job was posted. 
            l=driver.find_element(By.CSS_SELECTOR, ".css-y8sxh5:nth-child(2)")
            date=l.text
            job_posting_date.append(date)

            
            #lets also get the time in which a Particular Job was posted. 
            y=driver.find_element(By.CSS_SELECTOR, ".css-y8sxh5:nth-child(1)")
            t=y.text
            time_job_posted.append(t)

            
            #lets also get client's Major  captive Instruction. 
            captive=driver.find_element(By.CSS_SELECTOR, ".css-1sy5kfv")
            f=captive.text
            client_captive_instruction.append(f)

            
            #Lets also get the Field in which a  particular job lies into 
            field=driver.find_element(By.CSS_SELECTOR, ".css-n2t4wo")
            v=field.get_attribute('value')
            job_field.append(v)

            
            #lets now click the bid button.
            Bid_Button.click()
            time.sleep(5)
            price=driver.find_element(By.NAME,"teacher.forms.bid.payNow")

            
            #Getting clients Budget Per Each Particular Job Applied For. 
            my_bid_price=float(price.get_attribute('value'))
            My_Total_Budget=(my_bid_price)*2
            My_Bid_Amount.append(My_Total_Budget)
            time.sleep(5)
            driver.find_element(By.NAME,"teacher.forms.bid.payWhenDone").send_keys(my_bid_price)
            time.sleep(5)
            driver.find_element(By.XPATH, "/html/body/div[2]/div/div/form/input").click()
            time.sleep(5)
            driver.back()
            time.sleep(10)
    
            #If our bot does not find the "Bid Button,", then let it do what follows below here:
        except:
            print("Bid Already Placed")
            driver.back()
    print("Hey!, we are going on well, Give me a piece of mind and am gonna give you the best of me")
    #at this point i want to refresh the webpage now,  i want to refresh the webpage after every 5 seconds and bids for 
    #the jobs that will appear  
    while True:
        driver.refresh()
        time.sleep(5)
        new_jobs_list=[]
        new_jobs = driver.find_elements(By.CSS_SELECTOR, ".css-1xxbh89")
        for new in new_jobs:
            new_jobs_list.append(new.text)
        available = len(new_jobs)
        new_jobs=[]
        for n in new_jobs_list:
            if n not in old_jobs_list:
                new_jobs.append(n)
        The_jobs=len(new_jobs)
        if The_jobs==0:
            print("no new jobs available")
        #we may also need another loop here kindly. 
        else:
            # Load the sound file using a raw string literal
            sound_file = r"C:\Users\felix\Desktop\Application\App\mixkit-cartoon-toy-whistle-616.wav"  # replace with the full path to your sound file
            sound = pygame.mixer.Sound(sound_file)
            # Play the sound
            sound.play()
            print(The_jobs," jobs available")
            if available >0:
                My_Label=Label(Area,text="successfully logged in",bg="white",fg="blue")
                My_Label.place(x=10,y=250)
            else:
                while available==0:
                    try:
                        time.sleep(5)
                        driver.refresh()
                        time.sleep(5)
                        new_jobs = driver.find_elements(By.CSS_SELECTOR, ".css-1xxbh89")
                        for new in new_jobs:
                            new_jobs_list.append(new.text)
                        available = len(new_jobs)
                        if available >0:
                            break
                        else:
                            continue
                    except:
                        winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                        messagebox.showinfo("Co-Fiver Error", "Failed to identify new jobs even after the refresh")
                        driver.close()
            for i in range(The_jobs):
                
                #open a single job and bid for the Job.
                jobs = driver.find_elements(By.CSS_SELECTOR, ".css-1xxbh89")
                attempts=0
                max_attempt=5
                job = jobs[i]
                while attempts<max_attempt:
                    try:
                        for job in jobs:
                            jobii=job.text
                            if jobii not in old_jobs_list:
                                job.click()
                                break
                        break
                    except:
                        
                        print("unable to access job",i, "in attempt",attempts,"but i will keep on trying!!")
                        attempts+=1
                        time.sleep(7)
                time.sleep(5)
                #If the Bidding to a particular Job has not been done, let our bot bid for the job.
                refresh=0
                for x in range(100):
                    try:
                        Bid_Button=driver.find_element(By.XPATH, "//*[@id=\"main-question\"]/button")
                    
                        #Before Anything, lets first get  the clients Budget:
                        p=driver.find_element(By.CSS_SELECTOR, ".css-y8sxh5:nth-child(3)")
                        my_p=p.text
                        My_Client_Budget.append(my_p)
                        
                        #Lets get the date in which a particular job was posted. 
                        l=driver.find_element(By.CSS_SELECTOR, ".css-y8sxh5:nth-child(2)")
                        date=l.text
                        job_posting_date.append(date)
                    
                        #lets also get the time in which a Particular Job was posted. 
                        y=driver.find_element(By.CSS_SELECTOR, ".css-y8sxh5:nth-child(1)")
                        t=y.text
                        time_job_posted.append(t)
                    
                        #lets also get client's Major  captive Instruction. 
                        captive=driver.find_element(By.CSS_SELECTOR, ".css-1sy5kfv")
                        f=captive.text
                        client_captive_instruction.append(f)
                    
                        #Lets also get the Field in which a  particular job lies into 
                        field=driver.find_element(By.CSS_SELECTOR, ".css-n2t4wo")
                        v=field.get_attribute('value')
                        job_field.append(v)

                    
                        #lets now click the bid button.
                        Bid_Button.click()
                        time.sleep(5)
                        price=driver.find_element(By.NAME,"teacher.forms.bid.payNow")

                    
                        #Getting clients Budget Per Each Particular Job Applied For. 
                        my_bid_price=float(price.get_attribute('value'))
                        My_Total_Budget=(my_bid_price)*2
                        My_Bid_Amount.append(My_Total_Budget)
                        time.sleep(10)
                        driver.find_element(By.NAME,"teacher.forms.bid.payWhenDone").send_keys(my_bid_price)
                        time.sleep(5)
                        driver.find_element(By.XPATH, "/html/body/div[2]/div/div/form/input").click()
                        time.sleep(5)
                        driver.back()
                        time.sleep(5)
                        old_jobs_list.append(jobii)
                        break
                    except:
                        print("unable to find the elements in refresh",refresh,"but i will keep on trying")
                        refresh+=1
                        driver.refresh()
                        time.sleep(10)
            
                
                
#lets come up with start automation Button.
start_Bidding=Button(Area,width=20,pady=7,text="Start Bidding",bg="green",fg="white",border=3,command=automate)
start_Bidding.place(x=10,y=200)


#lets create a button to stop the bidding process.
stop_Bidding=Button(Area,width=20,pady=7,text="Stop Bidding",bg="red",fg="white",border=1)
stop_Bidding.place(x=200,y=200)



print("if008533")
print("C743186678s")


main_window.mainloop()

