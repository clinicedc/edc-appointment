from dateutil.relativedelta import relativedelta


class WindowPeriodHelper(object):
    """Class to manage an appointment's or visit's window period.

    An appointment datetime must fall within the date range
    determined by the lower and upper bounds set in the visit definition.
    """
    def __init__(self, visit_definition, appt_datetime, reference_datetime):
        self.error = None
        self.error_message = None
        self.visit_definition = visit_definition
        self.appt_datetime = appt_datetime
        self.reference_datetime = reference_datetime

    def check_datetime(self):
        """Checks if self.appt_datetime is within the scheduled visit window period.

        Args:
            self.reference_datetime: auto calculated / optimal timepoint datetime (best_appt_datetime)
            self.appt_datetime: user suggested datetime.
        """
        self.error = None
        self.error_message = None
        diff = 0  # always in days for now
        retval = True
        if not self.reference_datetime:
            raise TypeError(
                'Parameter \'self.reference_datetime\' cannot be None. Is appointment.best_appt_datetime = None?')
        # calculate the actual datetime for the window's upper and lower boundary relative to new_appt_datetime
        rdelta = relativedelta()
        setattr(rdelta, self.visit_definition.get_rdelta_attrname(
            self.visit_definition.upper_window_unit), self.visit_definition.upper_window)
        upper_window_datetime = self.reference_datetime + rdelta
        rdelta = relativedelta()
        setattr(rdelta, self.visit_definition.get_rdelta_attrname(
            self.visit_definition.lower_window_unit), self.visit_definition.lower_window)
        lower_window_datetime = self.reference_datetime - rdelta
        # count the timedelta between window's datetime and new appt datetime
        upper_td = self.appt_datetime - upper_window_datetime
        lower_td = self.appt_datetime - lower_window_datetime
        # get the units to display in the message
        upper_unit = self.visit_definition.get_rdelta_attrname(self.visit_definition.upper_window_unit)
        lower_unit = self.visit_definition.get_rdelta_attrname(self.visit_definition.lower_window_unit)
        if upper_td.days > 0:
            # past upper window boundary
            unit = upper_unit
            window_value = self.visit_definition.upper_window
            td_from_boundary = upper_td
            window_name = 'upper'
        elif lower_td.days < 0:
            # past lower window boundary
            unit = lower_unit
            window_value = self.visit_definition.lower_window
            td_from_boundary = upper_td
            window_name = 'lower'
        elif lower_td.days >= 0 and upper_td.days <= 0:
            # within window period
            unit = None
            window_value = None
            td_from_boundary = None
            window_name = None
            diff = 0
        else:
            raise TypeError()
        if td_from_boundary:
            diff = td_from_boundary.days  # TODO: this cannot be in days if unit is Hours
            retval = False
            self.error = True
            self.error_message = (
                'Datetime is out of {window_name} window period. Expected a datetime between {lower} and {upper}.'
                'Window allows {window_value} {unit}. Got {diff}.'.format(
                    lower=lower_window_datetime,
                    upper=upper_window_datetime,
                    window_name=window_name,
                    window_value=window_value,
                    unit=unit,
                    diff=diff))
        return retval