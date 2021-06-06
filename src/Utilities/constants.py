class Constants:
    """Klasa zawierająca stałe, które zostały wykorzystane podczas implementacji programu"""

    # stałe konfiguracyjne
    WINDOW_SIZE = "800x600"
    TEXT_WINDOW_TITLE = 'Platforma transakcyjna'

    # stałe odnoszące się do nazw pól tekstowych
    TEXT_MAIN_TITLE = 'Platforma transakcyjna Future Station'
    TEXT_MAIN_DESCRIPTION = 'Biuro maklerskie William-Scott Trade'
    TEXT_CLOSE_BUTTON = 'Wyjdź'
    TEXT_WITHDRAW_BUTTON = 'Wypłać'
    TEXT_WITHDRAW_ALL_BUTTON = 'Wypłać wszystkie środki'
    TEXT_DEPOSIT_BUTTON = 'Wpłać depozyt'
    TEXT_PURCHASE_SHARES_BUTTON = 'Zakup akcje'
    TEXT_AMOUNT = 'Kwota'
    TEXT_CURRENT_BALANCE = 'Saldo: '
    TEXT_VALUE_OF_SHARES_HELD = 'Wartość posiadanych akcji: '
    TEXT_TOTAL_ACCOUNT_VALUE = 'Wartość konta: '
    TEXT_CURRENCY = ' zł'  # waluta, w której obsługiwane są transakcje

    # stałe odnoszące się do zastosowanej palety kolorów
    COLOUR_BACKGROUND = '#2A2A2E'
    COLOUR_TEXT = '#FAFAFA'
    LISTBOX_SELECTION_BACKGROUND = '#800080'  # purple
    LISTBOX_TEXT_COLOUR = '#ffffff'  # light colour
    BUTTON_BACKGROUND_COLOUR = '#f1f1f1'

    # stałe odnoszące się do właściwości tekstu
    FONT_TYPEFACE = 'Ubuntu'
    FONT_WEIGHT_TITLE = 'bold'
    FONT_SIZE_TITLE = 20
    FONT_SIZE_DESCRIPTION = 14
    FONT_SIZE_REGULAR = 12

    # stałe odnoszące się do treści komunikatów
    MESSAGE_ERROR = 'Błąd'
    MESSAGE_ERROR_VALUE = 'Podano nieprawidłową wartość'
    MESSAGE_ERROR_NEGATIVE_BALANCE = 'Niewystarczająca ilość środków do wypłaty'
    MESSAGE_ERROR_NOT_ENOUGH_FUNDS = 'Niewystarczająca ilość środków do zakupu akcji'

    MESSAGE_CONFIRM_EXIT = 'Potwierdź wyjście'
    MESSAGE_CONFIRM_EXIT_TEXT = 'Czy na pewno chcesz opuścić platformę?'

    MESSAGE_CONFIRM_BUY_SHARES = 'Potwierdź zakup akcji'

    # stałe odnoszące się do statusu transakcji gotówkowych wybranego przez użytkownika
    DEPOSIT = 0  # chęć wpłaty
    WITHDRAWAL = 1  # chęć wypłaty
    WITHDRAWAL_ALL = 2  # chęć wypłaty wszystkich wolnych środków

    # separator danych stosowany podczas tworzenia listy firm
    DATA_SEPARATOR = ','

    # stałe odnoszące się do typów zleceń akcji
    BUY_ORDER = 'Zlecenie zakupu akcji'
    SELL_ORDER = 'Zlecenie sprzedaży akcji'

    # stałe dotyczące prowizji podczas wypłaty środków z konta
    WITHDRAWAL_COMMISSION_THRESHOLD = 300  # próg pobierania prowizji
    WITHDRAWAL_COMMISSION_AMOUNT = 30  # kwota prowizji podczas wypłaty poniżej progu

    ACTIVE_CURSOR = 'hand2'  # wygląd kursora po najechaniu na przyciski/listboxa

    # konfiguracja przycisków
    BUTTON_BORDER_SIZE = 0

    # konfiguracja list
    LISTBOX_WIDTH = 18
    LISTBOX_BORDER_SIZE = 0
    LISTBOX_HIGHLIGHT_THICKNESS = 0