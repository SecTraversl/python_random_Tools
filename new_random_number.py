# %%
#######################################
def new_random_number(size=None):
    """Creates a large random number string. You can specify the size of the number using the "size" parameter.

    Examples:
        >>> new_random_number()\n
        '88495077433033604864459347219444521153467941653074517'

        >>> new_random_number()\n
        '50687589765828927139866314225259581387781147585513699'

        >>> new_random_number()\n
        '3933481384'

        >>> new_random_number(size=333)\n
        '9714188696247383654871292573098225426647253076733397769390728697759149793081512588524364279370278384692180475130825330801079463843655342153603449199025254084984353138753538945813523746920322710962748572347098357639231982180325558624756995274493507086476515545437136794779622702572568526438176415058625571928676953194838042337245543725816954176121011728783177495855283625899367553099288845402459285860401135256887874543963892694098154533594068558877234595744195741767995977316325571867838167880357384194314525465248320818965444224623264936226428813528010558221318554454332511926659310098247750742688442346813527103355913470354848965473812'

        >>> new_random_number(size=123)\n
        '91214915252828538635886489742232177541769241334437959742634202621180775793449210509188183499799551465326960258663248621524515522562839393141151318716015189324901944462067354183367892964644774711423589068814314271621465396719985816232'

        >>> new_random_number(42)\n
        '577556851583248222148853278534675679332074959294122553484454275175328584499871890'

        >>> new_random_number(7)\n
        '18339518883949'


        Args:
            size (int, optional): Specify a desired number size. Defaults to None.

        Returns:
            str: Returns a long number string
    """
    import random

    if size:
        size_of_list = int(size)
    else:
        # Here we  create a list of up to 30 elements in size
        size_of_list = random.choice(range(1, 30))

    # The elements will be integers ranging from 1 to 100
    lst = list(range(1, 101))
    # From the "lst" of numbers 1 - 100, there will be multiple random choices, the quantity of which is based off of the number given to "k="
    random_list_of_ints = random.choices(lst, k=size_of_list)
    # Then we take that list of random numbers and join them together making one long string of digits
    big_random_number_string = "".join([str(e) for e in random_list_of_ints])
    return big_random_number_string

