
import re
name =  """
jpioasfjnmjnasfkjnasvhjksabvkhjsavbkjasdvbkjsdkjvbasdkvbsadkvksdavbsv
14541asf354saf53sa45f3241sa2vcas45v41sa35241v5as4v5sa45v456sdav45sdfvfdhjkhjkljk
fdsbfesbsfdbfsdkmbnsfdfbkfdbkfsdbksdfkbsdfkbsdfkbsdfkbsdafkmbfedkmabkefek;'kj'kk
nbfsdfbkfdbkfsdbksdfkbsdfkbsdfkbsdfkbsdafkmbfedkmabkefesafsafsafasfsafsfasfsafds
bfsdfbkfdbkfsdbksdfkbsdfkbsdfkbsdfkbsdafkmbfedkmabkefegbsdxgbsfdzbdfzbzdfbzfdbfd
bsdkfb ksdfgfbkfdbkfsdbksdfkbsdfkbsdfkbsdfkbsdafkmbfedkmabkefefgagerjiorejiolbkk
fbkfdbkfsdbksdfkbsdfkbsdfkbsdfkbsdafkmbfedkmabkefefbkfdbkfsdbksdfkbsdfkbsdfkbsdf
hasfahsfashfasfjasvochnikasvhnbiusdhavmynameiskevinjijsajfioasjfjfjfjnjvjvjvjjvj
ksdfkbsdfkf5as4f56sa4f5asvsdaklisadjviolasvilahsviwqbhfuhkgqwfuhgikfuhiduhfsuhfs
dsksdfkbsdfkksdfkbsdfkkwaofdjnmasvksdfkbsdfkksdfkbsdfkksdfkbsdfkkoasdjfksdfkbsdf
masjifnsvmynameisqqwweksdfkbsdfkksdfkbsdfkksdfkbsdfkksdfkbsdfkksdfkbsdfkksdfkbsd
"""
target  = re.findall("mynameis\w\w\w\w\w",name)


# using re.findall find pattrens that we wanted
