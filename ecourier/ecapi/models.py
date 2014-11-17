from django.db import models

# Create your models here.

class Gateway(models.Model):
    name = models.CharField(max_length=255)
    api = models.CharField(max_length=255)
    response = models.CharField(max_length=255)
  
    class Meta():
        ordering = ['name']

    
    

class UserGroup(models.Model):
    groups = models.CharField(max_length=255)


class Users(models.Model):
    user_id = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255) #username
    user_group = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)
    post_code = models.IntegerField()
    address = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'general_user'


    def __unicode__(self):
       return self.user_name

# 'TCS' : 'Traditional Courier Service'
#**** ChangeLog -+- Marchant -> Transporter
# |--> Find the files with Marchant included and replace with the Transporter

class Transporter(models.Model):
    name = models.CharField(max_length=255)
    company_name=models.CharField(max_length=255)
    group = models.CharField(max_length=255)
    MARCHENT_ID = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    post_code = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'transporter'
        
    def __unicode__(self):
       return self.name

class Parcel(models.Model):
    REFID = models.CharField(max_length=255)
    sendergroup = models.CharField(max_length=255)
    senderid = models.IntegerField(null=True,blank=True) # this should be integer field and match with the user group and id
    r_name = models.CharField(max_length=255)
    r_mobile = models.CharField(max_length=255)
    r_email = models.CharField(max_length=255)
    r_address = models.CharField(max_length=255)
    #r_product = models.CharField(max_length=255)
    r_price = models.IntegerField(null=True)
    r_type = models.CharField(max_length=255)
    #r_time = models.CharField(max_length=255)
    r_time = models.DateTimeField()
    r_loc_to = models.IntegerField()
    r_loc_from = models.IntegerField()
    status = models.CharField(max_length=255)
    timing = models.IntegerField(null=True)
    courier = models.IntegerField(null=True)
    agent = models.IntegerField(null=True)
    paymentmethod = models.CharField(max_length=255)
    billing = models.IntegerField(null=True)
    paymentclear = models.BooleanField(blank=True)
    comment = models.CharField(max_length=255,blank=True,null=True)
    
    def __unicode__(self):
       return self.REFID

class CourierParcelDesc(models.Model):
    REFID = models.ForeignKey(Parcel)
    sender_name = models.CharField(max_length=255)
    sender_mobile = models.CharField(max_length=255)
    sender_addr = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'courier_parcel_desc'
   
class ParcelDesc(models.Model):
    REFID = models.ForeignKey(Parcel)
    weight = models.IntegerField()
    shippingdistance = models.IntegerField()
    deleverytiming = models.IntegerField()
    time = models.CharField(max_length=255)
    comment = models.CharField(max_length=255)
    updatergroup = models.CharField(max_length=255)
    updaterid = models.CharField(max_length=255)
    
class ParcelPriceDesc(models.Model):
    REFID = models.ForeignKey(Parcel)
    weightprice = models.IntegerField()
    distanceprice = models.IntegerField()
    timingprice = models.IntegerField()
    totalprice = models.IntegerField()
    listprice = models.CharField(max_length=255)
    currency = models.CharField(max_length=255)
    paymentclear = models.BooleanField()
    paymentcollectorgorup = models.CharField(max_length=255)
    paymentcollectorid = models.CharField(max_length=255)
    time = models.CharField(max_length=255)

# change fields type   
class ParcelStatus(models.Model):
    REFID = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255)
    updatergroup = models.CharField(max_length=255)
    updaterid = models.CharField(max_length=255)
    loc = models.IntegerField(null=True,blank=True)
    comments = models.CharField(max_length=255)
    view = models.IntegerField()
    class Meta:
        db_table = 'parcelstatus'
    
class ParcelType(models.Model):
    type = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    params = models.CharField(max_length=255,null=True,blank=True)
    def __unicode__(self):
       return self.type
    
class Updater(models.Model):
    REFID = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True)
    updater = models.CharField(max_length=255)
    updaterid = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    loc = models.IntegerField()
    comments = models.CharField(max_length=255)
    
    def __unicode__(self):
       return self.status

class Notification(models.Model):
    n_from = models.IntegerField()
    usergroup = models.CharField(max_length=255)
    n_to = models.IntegerField()
    to_usergroup = models.CharField(max_length=255,null=True,blank=True)
    n_message = models.CharField(max_length=255)
    n_time = models.DateTimeField(auto_now_add=True)
    N_REFID = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    parcel = models.ForeignKey(Parcel)
    
    class Meta:
        db_table = 'notification'
    
    # add status code
    
# price table to add with customer order
# model class should be specific with each parcel type

class Parcel_Price():
    pass



    
class Ecommerce(models.Model):
    MARCHENTID = models.CharField(max_length=255)
    group = models.CharField(max_length=255)
    siteurl = models.CharField(max_length=255)
    loc = models.IntegerField()
    addr = models.CharField(max_length=255)
    email = models.EmailField()
    passwd = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    credits = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    date = models.CharField(max_length=255) # need to change
    
    api_secret = models.CharField(max_length=255,null=True,blank=True)
    api_key = models.CharField(max_length=255,null=True,blank=True)
    auth_token = models.CharField(max_length=255,null=True,blank=True)
    #price_table = models.ManyToManyField(EcommercePriceTable,null=True,blank=True)
    is_sms_on = models.BooleanField()
    
    def __unicode__(self):
       return self.siteurl
    
    
class Transporter_Branch(models.Model):
    name = models.CharField(max_length=255)
    passwd = models.CharField(max_length=255)
    loc = models.IntegerField()
    mar = models.ForeignKey(Transporter)
    mobile = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    addr = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    
class Transporter_Sub_Branch(models.Model):
    name = models.CharField(max_length=255)
    passwd = models.CharField(max_length=255)
    loc = models.IntegerField()
    mar = models.ForeignKey(Transporter_Branch)
    mobile = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    addr = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    
class Transporter_Branch_Map(models.Model):
    MAPID = models.CharField(max_length=255)
    loc = models.IntegerField()
    mar = models.ForeignKey(Transporter)
    addr = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    relation = models.CharField(max_length=255)
    
class Division(models.Model):
    name = models.CharField(max_length=255)
    def __unicode__(self):
       return self.name
    
class District(models.Model):
    name = models.CharField(max_length=255)
    division = models.ForeignKey(Division)
    def __unicode__(self):
       return self.name
    
class Thana(models.Model):
    name = models.CharField(max_length=255)
    district = models.ForeignKey(District)
    def __unicode__(self):
       return self.name

class PostOffice(models.Model):
    name = models.CharField(max_length=255)
    zip = models.IntegerField()
    thana = models.ForeignKey(Thana)
    def __unicode__(self):
       return self.name
    
class MailingAddress(models.Model):
    name = models.CharField(max_length=255)
    postOffice = models.ForeignKey(PostOffice)
    def __unicode__(self):
       return self.name

    
        
class log(models.Model):
    userid = models.CharField(max_length=255)
    act = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    ip = models.CharField(max_length=255)
    useragent = models.CharField(max_length=255)

class Route(models.Model):
    name = models.CharField(max_length=255)
    transporter = models.ForeignKey(Transporter)
    date = models.CharField(max_length=255)
    
class Emmiter(models.Model):
    pass

# ecourier agents
class Agent(models.Model):
    AGENTID = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    transporter = models.ForeignKey(Transporter)
    group = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)
    email = models.EmailField()
    loc = models.IntegerField()

    def __unicode__(self):
       return self.name
    
    
class ZoneMap(models.Model):
    name = models.CharField(max_length=255)
    post = models.ManyToManyField(PostOffice)
    totalarea = models.IntegerField(null=True,blank=True)
    
    class Meta:
        db_table = 'zonemap'
        
    def __unicode__(self):
       return self.name
   


# re-consideration of model design
class AgentCoverage(models.Model):
    model = 'AgentCoverage'
    agent = models.ForeignKey(Agent)
    zonemap = models.ForeignKey(ZoneMap)
    def __unicode__(self):
       return self.model

class XferCode(models.Model):
    transporter = models.ForeignKey(Transporter)
    group = models.CharField(max_length=50)
    agent = models.ForeignKey(Agent)
    agentid = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    
    def __unicode__(self):
       return self.code
    
class XferAllow(models.Model):
    code = models.ForeignKey(XferCode)
    agents = models.ManyToManyField(Agent,related_name='agent_allowed')    
   
class ParcelHandOver(models.Model):
    pass

class timeTest(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    
class UserPassword(models.Model):
    user_group = models.CharField(max_length=255)
    user_id = models.IntegerField(null=True,blank=True)
    user_name = models.CharField(max_length=255,null=True,blank=True)
    password = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'password'
        
    
class DeliveryTiming(models.Model):
    day = models.CharField(max_length=255)


    def __unicode__(self):
       return self.day
   
class Coverage(models.Model):
    place = models.CharField(max_length=255)
    def __unicode__(self):
       return self.place
   
class WeightLimit(models.Model):
    weight = models.CharField(max_length=255)
    def __unicode__(self):
       return self.weight
   
class EcommercePriceTable(models.Model):
    package_name = models.CharField(max_length=255)
    #ecommerce = models.ForeignKey(Ecommerce)
    day = models.ForeignKey(DeliveryTiming)
    place = models.ForeignKey(Coverage)
    weight = models.ForeignKey(WeightLimit)
    price = models.IntegerField()
    def __unicode__(self):
       return self.package_name
   
class EcommerceParcelDescription(models.Model):
    REFID = models.CharField(max_length=255)
    coverage = models.IntegerField(null=True,blank=True)
    timing = models.IntegerField(null=True,blank=True)
    weight = models.IntegerField(null=True,blank=True)
    parcel_price = models.IntegerField(null=True,blank=True)
    product_price = models.IntegerField(null=True,blank=True)
    cash_on_delivery = models.BooleanField(blank=True)
    shipping_agent = models.IntegerField(null=True,blank=True)
    monitoring_agent = models.IntegerField(null=True,blank=True)
    transporter = models.IntegerField(null=True,blank=True)
    is_clear = models.BooleanField(blank=True)
    comment = models.CharField(max_length=255,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
   
    class Meta:
        db_table = 'EcommerceParcelDescription'
        ordering = ['created_at']
        
    def __unicode__(self):
       return self.REFID
