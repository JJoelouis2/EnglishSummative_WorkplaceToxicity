import kivy
import webbrowser
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.core.window import Window

# Set the window size
Window.size = (1152, 648)

def hyperlink(instance, domain):
    """
    Template for hyperlink buttons
        self.reflection_button.bind(on_release=lambda x: hyperlink(x, ""))
    """
    webbrowser.open(domain)

class EnglishSummative(FloatLayout):
    def __init__(self, **kwargs):
        super(EnglishSummative, self).__init__(**kwargs)

        # Background image filling the whole screen
        home_image = Image(source="workplace_toxicity_menu.png", allow_stretch=True, keep_ratio=False, size_hint=(1, 1))
        self.add_widget(home_image)

        # Self-reflection button
        self.reflection_button = Button(size_hint=(None, None), size=(1000, 180), 
                       pos_hint={'center_x': 0.26, 'center_y': 0.65}, background_normal='',  
                       background_color=(0, 0, 0, 0))
        self.add_widget(self.reflection_button)
        self.reflection_button.bind(on_press=self.reflection)
        

        # Stories button
        self.stories_button = Button(size_hint=(None, None), size=(1000, 187),
                       pos_hint={'center_x': 0.26, 'center_y': 0.3775}, background_normal='',  
                       background_color=(0, 0, 0, 0))
        self.add_widget(self.stories_button)
        self.stories_button.bind(on_press=self.stories)

        # Resources button
        self.resources_button = Button(size_hint=(None, None), size=(1000, 167),
                       pos_hint={'center_x': 0.26, 'center_y': 0.115}, background_normal='',  
                       background_color=(0, 0, 0, 0))
        self.add_widget(self.resources_button)    
        self.resources_button.bind(on_press=self.resources)

        # Back button
        self.back_button = Button(size_hint=(None, None), size=(220, 95), 
                       pos_hint={'center_x': 0.04, 'center_y': 0.95}, background_normal='',  
                    background_color=(0, 0, 0, 0))
        self.back_button.bind(on_press=lambda x: self.__init__())

    def reflection(self, instance):
        self.clear_widgets()

        # Self-reflection image
        reflection_image = Image(source="workplace_toxicity_reflection1.png", allow_stretch=True, keep_ratio=False, size_hint=(1, 1))
        self.add_widget(reflection_image)

        # Back button
        self.add_widget(self.back_button)

        # Continue button
        self.continue_button = Button(size_hint=(None, None), size=(273, 98),
                       pos_hint={'center_x': 0.12, 'center_y': 0.055}, background_normal='',  
                       background_color=(0, 0, 0, 0))
        self.add_widget(self.continue_button)    
        self.continue_button.bind(on_press=self.reflection2)

        # Responses form button
        self.responses_form_button = Button(size_hint=(None, None), size=(75, 98),
                       pos_hint={'center_x': 0.725, 'center_y': 0.055}, background_normal='',  
                       background_color=(0, 0, 0, 0))
        self.add_widget(self.responses_form_button)   
        self.responses_form_button.bind(on_release=lambda x: hyperlink(x, "https://docs.google.com/forms/d/e/1FAIpQLSeUNVqOa6kwtWiIrBXA-aXPqPdNPX9aQYN-zQs-z5CPLsAEkA/viewform?usp=dialog"))

    def reflection2(self, instance):
        self.clear_widgets()

        # Self-reflection image
        reflection_image = Image(source="workplace_toxicity_reflection2.png", allow_stretch=True, keep_ratio=False, size_hint=(1, 1))
        self.add_widget(reflection_image)

        # Back button back to first reflection page
        self.back_reflection_button = Button(size_hint=(None, None), size=(220, 95), 
                       pos_hint={'center_x': 0.04, 'center_y': 0.95}, background_normal='',  
                       background_color=(0, 0, 0, 0))
        self.add_widget(self.back_reflection_button) 
        self.back_reflection_button.bind(on_press=self.reflection)      

        # Response form button
        self.add_widget(self.responses_form_button)

    def stories(self, instance):
        self.clear_widgets()

        # Stories image
        stories_image = Image(source="workplace_toxicity_stories.png", allow_stretch=True, keep_ratio=False, size_hint=(1, 1))
        self.add_widget(stories_image)

        # Back button
        self.add_widget(self.back_button)
    
        # Susan's story button
        susan_button = Button(size_hint=(None, None), size=(275, 275), 
                       pos_hint={'center_x': 0.125, 'center_y': 0.63}, background_normal='',  
                       background_color=(0, 0, 0, 0))
        self.add_widget(susan_button)
        susan_button.bind(on_release=lambda x: hyperlink(x, "https://www.workplacebullyingcoalition.org/susan-s-story"))

        # Sherry's story button
        sherry_button = Button(size_hint=(None, None), size=(275, 275), 
                       pos_hint={'center_x': 0.37, 'center_y': 0.63}, background_normal='',  
                       background_color=(0, 0, 0, 0))
        self.add_widget(sherry_button)
        sherry_button.bind(on_release=lambda x: hyperlink(x, "https://tedxwinnipeg.ca/speaker/sherry-lee-benson-podolchuk/"))

        # Jessica's story button
        jessica_button = Button(size_hint=(None, None), size=(275, 275), 
                       pos_hint={'center_x': 0.61, 'center_y': 0.63}, background_normal='',  
                       background_color=(0, 0, 0, 0))
        self.add_widget(jessica_button)
        jessica_button.bind(on_release=lambda x: hyperlink(x, "https://www.linkedin.com/pulse/my-personal-experience-workplace-bullying-adult-jessica-bellingham/"))

        # Lewis's story button
        lewis_button = Button(size_hint=(None, None), size=(275, 275), 
                       pos_hint={'center_x': 0.23, 'center_y': 0.25}, background_normal='',  
                       background_color=(0, 0, 0, 0))
        self.add_widget(lewis_button)
        lewis_button.bind(on_release=lambda x: hyperlink(x, "https://www.youtube.com/watch?v=-FG_wjILGOg"))

        # Lewis's story button
        mark_button = Button(size_hint=(None, None), size=(275, 275), 
                       pos_hint={'center_x': 0.475, 'center_y': 0.25}, background_normal='',  
                       background_color=(0, 0, 0, 0))
        self.add_widget(mark_button)
        mark_button.bind(on_release=lambda x: hyperlink(x, "https://timothydimoff.com/2020/10/23/personal-account-workplace-bullying/"))

        # Laura's story button
        laura_button = Button(size_hint=(None, None), size=(275, 275), 
                       pos_hint={'center_x': 0.73, 'center_y': 0.25}, background_normal='',  
                       background_color=(0, 0, 0, 0))
        self.add_widget(laura_button)
        laura_button.bind(on_release=lambda x: hyperlink(x, "https://www.youtube.com/watch?v=XlpVTyprp9M"))

        # Sharing story button
        share_story = Button(size_hint=(None, None), size=(275, 275), 
                       pos_hint={'center_x': 0.855, 'center_y': 0.63}, background_normal='',  
                       background_color=(0, 0, 0, 0))
        self.add_widget(share_story)
        share_story.bind(on_release=lambda x: hyperlink(x, "https://docs.google.com/forms/d/e/1FAIpQLScp0eA5my9rgZFpnGUzNRw85WlC2C8HdHFtUKuPt1z2W7QkgQ/viewform?usp=dialog"))
        
    def resources(self, instance):
        self.clear_widgets()

        # Resources image
        resources_image = Image(source="workplace_toxicity_resources.png", allow_stretch=True, keep_ratio=False, size_hint=(1, 1))
        self.add_widget(resources_image)

        # Back button
        self.add_widget(self.back_button)

        # Attorney button
        self.attorneys_button = Button(size_hint=(None, None), size=(380, 380),
                       pos_hint={'center_x': 0.15, 'center_y': 0.5}, background_normal='',  
                       background_color=(0, 0, 0, 0))
        self.add_widget(self.attorneys_button)    
        self.attorneys_button.bind(on_press=self.attorneys)

        # Health resources button
        self.health_resources_button = Button(size_hint=(None, None), size=(380, 380),
                       pos_hint={'center_x': 0.5, 'center_y': 0.5}, background_normal='',  
                       background_color=(0, 0, 0, 0))
        self.add_widget(self.health_resources_button)
        self.health_resources_button.bind(on_press=self.health_resources)

    def attorneys(self, instance):
        self.clear_widgets()

        # Attorney image
        attorneys_image = Image(source="workplace_toxicity_attorneys.png", allow_stretch=True, keep_ratio=False, size_hint=(1, 1))
        self.add_widget(attorneys_image)

        # Back to resources button
        self.back_resources_button = Button(size_hint=(None, None), size=(220, 95), 
                       pos_hint={'center_x': 0.04, 'center_y': 0.95}, background_normal='',  
                       background_color=(0, 0, 0, 0))
        self.add_widget(self.back_resources_button)
        self.back_resources_button.bind(on_press=self.resources)

        # Brooker Law button
        self.brooker_button = Button(size_hint=(None, None), size=(240, 240), 
                       pos_hint={'center_x': 0.14, 'center_y': 0.65}, background_normal='',  
                       background_color=(0, 0, 0, 0))
        self.add_widget(self.brooker_button)
        self.brooker_button.bind(on_release=lambda x: hyperlink(x, "https://www.brookerlawoffice.ca/employment-law/workplace-harassment/"))

        # Aaron Waxman & Associates button
        self.aaron_button = Button(size_hint=(None, None), size=(240, 240), 
                       pos_hint={'center_x': 0.38, 'center_y': 0.65}, background_normal='',  
                       background_color=(0, 0, 0, 0))
        self.add_widget(self.aaron_button)
        self.aaron_button.bind(on_release=lambda x: hyperlink(x, "https://www.awaxmanlaw.ca/employment/bullying-harassment"))

        # Lecker & Associates button
        self.lecker_button = Button(size_hint=(None, None), size=(240, 240), 
                       pos_hint={'center_x': 0.625, 'center_y': 0.65}, background_normal='',  
                       background_color=(0, 0, 0, 0))
        self.add_widget(self.lecker_button)
        self.lecker_button.bind(on_release=lambda x: hyperlink(x, "https://leckerslaw.com/employment-lawyers-ottawa/"))

        # Ontario Human Rights Commission button
        self.ontario_button = Button(size_hint=(None, None), size=(240, 240), 
                       pos_hint={'center_x': 0.875, 'center_y': 0.65}, background_normal='',  
                       background_color=(0, 0, 0, 0))
        self.add_widget(self.ontario_button)
        self.ontario_button.bind(on_release=lambda x: hyperlink(x, "https://www3.ohrc.on.ca/en/contact-us"))

    def health_resources(self, instance):
        self.clear_widgets()

        # Health resources image
        health_resources_image = Image(source="workplace_toxicity_health.png", allow_stretch=True, keep_ratio=False, size_hint=(1, 1))
        self.add_widget(health_resources_image)

        # Back to resources button
        self.back_resources_button = Button(size_hint=(None, None), size=(220, 95), 
                       pos_hint={'center_x': 0.04, 'center_y': 0.95}, background_normal='',  
                       background_color=(0, 0, 0, 0))
        self.add_widget(self.back_resources_button)
        self.back_resources_button.bind(on_press=self.resources)

        # Health and Safety centre button
        self.health_safety_button = Button(size_hint=(None, None), size=(350, 220), 
                       pos_hint={'center_x': 0.15, 'center_y': 0.66}, background_normal='',  
                       background_color=(0, 0, 0, 0))
        self.add_widget(self.health_safety_button)
        self.health_safety_button.bind(on_release=lambda x: hyperlink(x, "https://www.ontario.ca/page/filing-workplace-health-and-safety-complaint"))
        
        # Canadian Mental Health Association button
        self.canadian_button = Button(size_hint=(None, None), size=(285, 220), 
                       pos_hint={'center_x': 0.41, 'center_y': 0.66}, background_normal='',  
                       background_color=(0, 0, 0, 0))
        self.add_widget(self.canadian_button)
        self.canadian_button.bind(on_release=lambda x: hyperlink(x, "https://cmha.ca/"))

        # Think Mental Health button
        self.think_button = Button(size_hint=(None, None), size=(293, 220), 
                       pos_hint={'center_x': 0.663, 'center_y': 0.66}, background_normal='',  
                       background_color=(0, 0, 0, 0))
        self.add_widget(self.think_button)
        self.think_button.bind(on_release=lambda x: hyperlink(x, "https://thinkmentalhealth.ca/"))

        # Convex Ontario button
        self.convex_button = Button(size_hint=(None, None), size=(220, 220), 
                       pos_hint={'center_x': 0.8775, 'center_y': 0.66}, background_normal='',  
                       background_color=(0, 0, 0, 0))
        self.add_widget(self.convex_button)
        self.convex_button.bind(on_release=lambda x: hyperlink(x, "https://connexontario.ca/?utm_source=google&utm_medium=organic&utm_campaign=Google%20My%20Business&utm_content=website"))

class RunApp(App):
    def build(self):
        return EnglishSummative()

if __name__ == "__main__":
    RunApp().run()