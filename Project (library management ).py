#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
df=pd.DataFrame()
df=pd.read_csv("C:/Users/admin/Downloads/Telegram Desktop/Book_Information csv.csv")
print(df)


# In[14]:


import pandas as pd
df=pd.DataFrame()
df=pd.read_csv("C:/Users/admin/Downloads/Telegram Desktop/Cost_Management.csv")
print(df)



# In[16]:


import pandas as pd
df=pd.DataFrame()
df=pd.read_csv("C:/Users/admin/Downloads/Telegram Desktop/Holders_Information.csv")
print(df)


# In[27]:


import pandas as pd 
import matplotlib.pyplot as plt 
df=pd.read_csv("C:/Users/admin/Downloads/Telegram Desktop/Cost_Management.csv")
#Creating a bar graph
plt.bar(df["Book ID"],df["Cost"])
#Labels and titles etc things 
plt.xlabel("BOOK ID")
plt.ylabel("Cost")
plt.title("Comparission of Book ID v/s Cost")
plt.xticks(rotation=45,ha="right")
#complete !
plt.show()


# In[32]:


import pandas as pd 
import matplotlib.pyplot as plt 
df=pd.read_csv("C:/Users/admin/Downloads/Telegram Desktop/Book_Information csv.csv")
#count Genre
genre_count=df['Genre'].value_counts()
#creating a pie chart 
plt.pie(genre_count,labels = genre_count.index , startangle=90)
#title
plt.title("Share Holding of Different Books in Library")
#Complete !
plt.show()


# In[37]:


import pandas as pd 
import matplotlib.pyplot as plt 
df=pd.read_csv("C:/Users/admin/Downloads/Telegram Desktop/Cost_Management.csv")
plt.plot(df["Book ID"],df["Servicing Cost"], marker= 'o',linestyle="--", linewidth=2,markersize=8)
#editing 
plt.xticks(rotation=45,ha="right")
#complete !
plt.show()


# In[40]:


import pandas as pd 
import matplotlib.pyplot as plt 
df= pd.read_csv("C:/Users/admin/Downloads/Telegram Desktop/Cost_Management.csv")
#creating a bar graph 
plt.bar(df["Book ID"],df["Total Rent Collected"])
#Touch up 
plt.xlabel("BOOK ID")
plt.ylabel("Total Rent collected")
plt.title("Total Rent collected v/s Book ID ")
plt.xticks(rotation=45,ha="right")
#completed !
plt.show()


# In[49]:


import pandas as pd
import matplotlib.pyplot as plt 
df= pd.read_csv("C:/Users/admin/Downloads/Telegram Desktop/Cost_Management.csv")
#Creation 
plt.hist(df["Total Rent Collected"], bins = 6, alpha = 0.7, edgecolor="black")
#Touch up
plt.xlabel("Total Rent Collected")
plt.ylabel("number of Books")
plt.show()


# In[ ]:




