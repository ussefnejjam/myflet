from flet import *
def main(page:Page):
    page.title="chatapp"
    page.window.height=740
    page.bgcolor="#6667AB"
    page.window.width=390
    page.window.top =10
    page.window.left=960
    page.vertical_alignment="center"
    page.horizontal_alignment="center"
    page.appbar=AppBar(
bgcolor="#CC2936",title=Text("𝙇𝙤𝙜𝙞𝙣 𝙎𝙮𝙩𝙚𝙢"),center_title=True,
leading=Icon(icons.HOME),leading_width=40,actions=[IconButton(icons.NOTIFICATIONS),PopupMenuButton(
items=[PopupMenuItem(text="PROFILE"),PopupMenuItem(text="SUPPORT")
,PopupMenuItem(text="DONATE"),PopupMenuItem(text="SETTING"),
PopupMenuItem(text="ABOUT US"),PopupMenuItem(text=""),PopupMenuItem(text="EXIT",)])])
    def show(e):
        v1=en1.value
        v2=en2.value
        if v1=='ussef' and v2=='dragons':
            alert1=AlertDialog(
                title=Text("Welcome Admin",size=18,color='green'))
            page.overlay.append(alert1)
            alert1.open=True
            page.update()
        else :
            alert1=AlertDialog(
                title=Text("Data Error",size=18,color='red'))
            page.overlay.append(alert1)
            alert1.open=True
            page.update()
        
        






    image=Image(src="logo.png",width=170)
    text=Text("𝑨𝑫𝑴𝑰𝑵",color='white',size=(25))
    en1=TextField(label='Email',icon=icons.EMAIL)
    en2=TextField(label='Password',icon=icons.PASSWORD,password=True,can_reveal_password=True)

    btn1=ElevatedButton('𝑳𝑶𝑮𝑰𝑵',on_click=show)






    page.add(image,text,en1,en2,btn1)



    page.navigation_bar=CupertinoNavigationBar(bgcolor="#CC2936",inactive_color=colors.BLACK,destinations=[NavigationBarDestination(icon=icons.CALL),
NavigationBarDestination(icon=icons.CAMERA),NavigationBarDestination(icon=icons.CONTACT_PHONE)])

















    page.update()
app(main)
