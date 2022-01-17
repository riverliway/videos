from manim import *
import random, math

TITLE_COLOR = "#91caed"

class AutomataDiagram(Scene):
    def construct(self):
        self.theory_of_computation()
        current_rect, group = self.comb_logic()
        group = self.fsm(group)
        group = self.pushdown(group)
        group = self.turing(group)

        self.wait()
        group = self.highlight(current_rect, group)
        self.wait()

    def theory_of_computation(self):
        bg = ImageMobject("..\\..\\..\\assets\\manim_bg.png")
        self.add(bg)
        toc = Text("Theory of Computation", font="Oxygen Bold", color=TITLE_COLOR)
        self.play(Write(toc))
        self.play(toc.animate.shift(UP * 3))
        self.play(Write(Underline(toc)))

    def comb_logic(self):
        comb = Text("Combinatorial Logic", font="Oxygen")
        comb_rect = RoundedRectangle(corner_radius=0.5, width=7)
        self.play(Create(comb_rect), Write(comb))

        comb_box = Group(comb_rect, comb)
        self.play(comb_box.animate.scale(0.7).shift(RIGHT * 0.5 + DOWN))

        return comb_rect, comb_box

    def fsm(self, group):
        fsm = Text("Finite State Machines", font="Oxygen")
        fsm = fsm.shift(UP * 0.5 + LEFT * 0.5).scale(0.7)
        fsm_rect = RoundedRectangle(corner_radius=0.5, width=6.5, height=3).shift(DOWN * 0.5)
        self.play(Write(fsm), Create(fsm_rect))

        box = Group(group, fsm, fsm_rect)
        self.play(box.animate.scale(0.75).shift(RIGHT * 0.46 + DOWN * 0.75))

        return box

    def pushdown(self, group):
        pushd = Text("Pushdown Automata", font="Oxygen")
        pushd = pushd.shift(UP * 0.3 + LEFT * 1.1).scale(0.7 * 0.75)
        pushd_rect = RoundedRectangle(corner_radius=0.5, width=6.5, height=3.3).shift(DOWN)
        self.play(Write(pushd), Create(pushd_rect))

        box = Group(group, pushd, pushd_rect)
        self.play(box.animate.scale(0.75).shift(RIGHT * 0.6, DOWN * 0.2))

        return box

    def turing(self, group):
        turing = Text("Turing Machines", font="Oxygen")
        turing = turing.shift(UP * 0.305 + LEFT * 1.8).scale(0.7 * 0.75 * 0.75)
        turing_rect = RoundedRectangle(corner_radius=0.5, width=6.5, height=3.3).shift(DOWN)
        self.play(Write(turing), Create(turing_rect))

        box = Group(group, turing, turing_rect)
        return box

    def highlight(self, current_rect, group):
        filled_rect = current_rect.copy()
        filled_rect.set_opacity(0.5)
        filled_rect.set_fill(BLUE_E)
        self.play(Transform(current_rect, filled_rect))
        self.wait()

        box = Group(filled_rect, group)
        return box

class Binary(Scene):
    def construct(self):
        bg = ImageMobject("..\\..\\..\\assets\\manim_bg.png")
        self.add(bg)
        computer = ImageMobject("..\\..\\..\\assets\\computer-avatar.png").scale(0.5)
        self.add(computer)
        title, underline = self.defining_computation()
        self.binary(computer)

        self.play(FadeOut(title), FadeOut(underline), FadeOut(computer))

    def defining_computation(self):
        title = Text("Defining Computation", font="Oxygen", color=TITLE_COLOR)
        title.shift(UP * 3)
        underline = Underline(title)
        self.play(Write(title), Write(underline))
        self.wait()

        return title, underline

    def binary(self, computerImage):
        def generate_stream():
            NUM_BITS = 500
            stream = ""

            for _ in range(NUM_BITS):
                stream += random.choice(["0", "1"])

            return stream

        NUM_STREAMS = 3
        streams = [Text(generate_stream(), font="Oxygen").scale(0.6).shift((i - (NUM_STREAMS - 1) / 2) * 0.8) for i in range(NUM_STREAMS)]
        fadein_animations = [FadeIn(stream) for stream in streams]
        self.remove(computerImage)
        self.play(fadein_animations[0], fadein_animations[1], fadein_animations[2], Wiggle(computerImage))
        self.wait()

        def shift_stream():
            shifts = [random.uniform(-2.5, 2.5) for _ in range(NUM_STREAMS)]
            shift_animations = [streams[i].animate.shift(RIGHT * shifts[i]) for i in range(NUM_STREAMS)]
            self.play(shift_animations[0], shift_animations[1], shift_animations[2])

        NUM_SHIFTS = 6
        for _ in range(NUM_SHIFTS):
            shift_stream()
            self.wait(0.15)
        
        self.wait()

        fadeout_animations = [FadeOut(stream) for stream in streams]
        self.play(fadeout_animations[0], fadeout_animations[1], fadeout_animations[2])

class TriangleTest(Scene):
    def construct(self):
        bg = ImageMobject("..\\..\\..\\assets\\manim_bg.png")
        self.add(bg)

        self.add(Line(start=ORIGIN, end=DOWN))
        self.add(Triangle().rotate(30 * DEGREES).scale(0.53).shift(0.53 * DOWN + 0.02 * RIGHT))

class CircuitTrace(Scene):
    def construct(self):
        bg = ImageMobject("..\\..\\..\\assets\\manim_bg.png")
        self.add(bg)

        self.binary_sequence()
        self.create_circuit()

        self.wait()

    def binary_sequence(self):
        sequence = "1011001"
        width = lambda x: RIGHT * 0.4 * (x - len(sequence) / 2)
        texts = [Text(bit, font="Oxygen").shift(width(index)) for index, bit in enumerate(sequence)]
        
        textsGroup = VGroup()
        for t in texts:
            textsGroup.add(t)

        self.play(Write(textsGroup))
        self.wait()

        height = lambda x: LEFT * 4.5 + (x - (len(sequence) - 1) / 2) * DOWN - width(x)

        for index, text in enumerate(texts):
            self.play(text.animate.shift(height(index)), run_time=0.2)

        self.wait()

    def create_circuit(self):
        circles = [Circle(radius=0.1, color=WHITE).shift(LEFT * 3.7 + DOWN * i) for i in range(-3, 4)]
        circleGroup = VGroup()
        for c in circles:
            circleGroup.add(c)

        self.play(Create(circleGroup, lag_ratio=0.2))

        first_gates, first_lines = self.create_first_layer()
        second_gates, second_lines = self.create_second_layer(first_gates)
        third_gate, third_lines = self.create_third_layer(second_gates)
        self.create_connections(first_lines, second_lines, third_lines, third_gate)

    def create_first_layer(self):
        gates = []
        and_gate = AndGate()
        and_gate.scale(0.5)
        and_gate.shift(3.25 * UP + 2.5 * LEFT)
        gates.append(and_gate)

        or_gate = OrGate()
        or_gate.scale(0.5)
        or_gate.shift(1.25 * UP + 2.5 * LEFT)
        gates.append(or_gate)

        xor_gate = XorGate()
        xor_gate.scale(0.5)
        xor_gate.shift(0.75 * DOWN + 2.5 * LEFT)
        gates.append(xor_gate)

        not_gate = NotGate()
        not_gate.scale(0.5)
        not_gate.shift(2.25 * DOWN + 2.5 * LEFT)
        gates.append(not_gate)
        self.play(AnimationGroup(*[Create(gate.get_group()) for gate in gates], lag_ratio=0.2))

        lines = []
        p1 = 3 * UP + 3.6 * LEFT
        p2 = and_gate.get_top_input()
        lines.append(horizontal_zline(p1, p2))

        p1 = 2 * UP + 3.6 * LEFT
        p2 = and_gate.get_bot_input()
        lines.append(horizontal_zline(p1, p2))

        p1 = UP + 3.6 * LEFT
        p2 = or_gate.get_top_input()
        lines.append(horizontal_zline(p1, p2))

        p1 = 3.6 * LEFT
        p2 = or_gate.get_bot_input()
        lines.append(horizontal_zline(p1, p2))

        p1 = -UP + 3.6 * LEFT
        p2 = xor_gate.get_top_input()
        lines.append(horizontal_zline(p1, p2))

        p1 = 2 * -UP + 3.6 * LEFT
        p2 = xor_gate.get_bot_input()
        lines.append(horizontal_zline(p1, p2))

        lines.append(Line(start=-3 * UP + 3.6 * LEFT, end=not_gate.get_top_input()))

        return gates, lines

    def create_second_layer(self, first_gates):
        gates = []
        xor_gate = XorGate()
        xor_gate.scale(0.5)
        xor_gate.shift(2.25 * UP + 0.5 * LEFT)
        gates.append(xor_gate)

        and_gate = AndGate()
        and_gate.scale(0.5)
        and_gate.shift(1.5 * DOWN + 0.5 * LEFT)
        gates.append(and_gate)
        self.play(AnimationGroup(*[Create(gate.get_group()) for gate in gates], lag_ratio=0.2))

        lines = []
        p1 = first_gates[0].get_output()
        p2 = xor_gate.get_top_input()
        lines.append(horizontal_zline(p1, p2))

        p1 = first_gates[1].get_output()
        p2 = xor_gate.get_bot_input()
        lines.append(horizontal_zline(p1, p2))

        p1 = first_gates[2].get_output()
        p2 = and_gate.get_top_input()
        lines.append(horizontal_zline(p1, p2))

        p1 = first_gates[3].get_output()
        p2 = and_gate.get_bot_input()
        lines.append(horizontal_zline(p1, p2))

        return gates, lines

    def create_third_layer(self, second_gates):
        or_gate = OrGate()
        or_gate.scale(0.5)
        or_gate.shift(0.5 * UP + 1.5 * RIGHT)
        self.play(Create(or_gate.get_group()))
        
        lines = []
        p1 = second_gates[0].get_output()
        p2 = or_gate.get_top_input()
        lines.append(horizontal_zline(p1, p2))

        p1 = second_gates[1].get_output()
        p2 = or_gate.get_bot_input()
        lines.append(horizontal_zline(p1, p2))

        return or_gate, lines

    def create_connections(self, lines1, lines2, lines3, last_gate):
        self.play(AnimationGroup(*[Create(zline) for zline in lines1]))
        self.play(AnimationGroup(*[Create(zline) for zline in lines2]))
        self.play(AnimationGroup(*[Create(zline) for zline in lines3]))

        end_point = last_gate.get_output() + RIGHT
        line = Line(start=last_gate.get_output(), end=end_point)
        circle = Circle(radius=0.1, color=WHITE).shift(end_point + RIGHT * 0.1)
        self.play(Create(line, run_time=0.5))
        self.play(Create(circle, run_time=0.5))

        output = Text("1", font="Oxygen").shift(end_point + 0.7 * RIGHT)
        self.play(Write(output))

class Gate:
    def __init__(self):
        self.group = VGroup()
        self.top_input = None
        self.bot_input = None
        self.output = None

    def get_group(self):
        return self.group

    def add_inputs_to_group(self):
        self.group.add(self.top_input)
        if self.bot_input is not None:
            self.group.add(self.bot_input)
        self.group.add(self.output)

    def get_top_input(self):
        return self.top_input.get_midpoint()

    def get_bot_input(self):
        return self.bot_input.get_midpoint()

    def get_output(self):
        return self.output.get_midpoint()

    def scale(self, value):
        self.group.scale(value)

    def shift(self, value):
        self.group.shift(value)

class NotGate(Gate):
    def __init__(self):
        super().__init__()

        THICK = 1.5
        RADIUS = 0.1
        shift = 0.53 * DOWN * THICK + RIGHT * 0.24
        self.group.add(Triangle(color=WHITE).rotate(30 * DEGREES).scale(0.53 * THICK).shift(shift))
        #self.group.add(Line(start=ORIGIN, end=THICK * DOWN))
        tip = RIGHT * (THICK * math.sqrt(3) / 2 + 0.04) + THICK * DOWN / 2
        #self.group.add(Line(start=THICK * DOWN, end=tip))
        #self.group.add(Line(start=tip, end=ORIGIN))
        self.group.add(Circle(radius=RADIUS, color=WHITE).shift(tip + RADIUS * RIGHT))

        self.top_input = Dot(point=DOWN * THICK / 2, fill_opacity=0)
        self.output = Dot(point=tip + 3 * RADIUS * RIGHT, fill_opacity=0)

        self.add_inputs_to_group()

class AndGate(Gate):
    def __init__(self):
        super().__init__()

        THICK = 1.5
        WIDTH = DOWN * THICK
        OFFSET = 0.04
        self.group.add(Line(start=ORIGIN, end=WIDTH))
        self.group.add(Line(start=WIDTH + OFFSET * LEFT, end=WIDTH+RIGHT))
        self.group.add(Arc(start_angle=-PI/2, angle=PI, radius=THICK * 0.5).shift(WIDTH * 0.5 + RIGHT))
        self.group.add(Line(start=RIGHT, end=OFFSET * LEFT))

        self.top_input = Dot(point=WIDTH / 4, fill_opacity=0)
        self.bot_input = Dot(point=3 * WIDTH / 4, fill_opacity=0)
        self.output = Dot(point=RIGHT * (1 + THICK / 2) + WIDTH / 2 + RIGHT * 0.1, fill_opacity=0)

        self.add_inputs_to_group()

    def calculate(self, in1, in2):
        return in1 and in2

class OrGate(Gate):
    def __init__(self):
        super().__init__()

        THICK = 1.5     # How thick the gate is (height)
        SIZE = 0.6      # How big the gate is (length)
        WIDTH = DOWN * THICK
        LENGTH = RIGHT * SIZE
        OFFSET = 0.03

        self.group.add(garc(ORIGIN, WIDTH, 1))
        self.group.add(Line(start=WIDTH + OFFSET * LEFT, end=WIDTH + LENGTH))

        tip = WIDTH / 2 + LENGTH * 3
        self.group.add(garc(WIDTH + LENGTH, tip, -1))
        self.group.add(garc(tip, LENGTH, -1))

        self.group.add(Line(start=LENGTH, end=OFFSET * LEFT))

        c = math.dist(ORIGIN, WIDTH)
        r = math.hypot(c/2, 1)
        d = math.sqrt(r ** 2 - (c / 4) ** 2) - 1
        self.top_input = Dot(point=RIGHT * d + WIDTH / 4, fill_opacity=0)
        self.bot_input = Dot(point=RIGHT * d + 3 * WIDTH / 4, fill_opacity=0)
        self.output = Dot(point=tip + RIGHT * 0.1, fill_opacity=0)

        self.add_inputs_to_group()

    def calculate(self, in1, in2):
        return in1 or in2

class XorGate(OrGate):
    def __init__(self):
        super().__init__()

        OFFSET = 0.4
        THICK = 1.5     # How thick the gate is (height)
        WIDTH = DOWN * THICK
        self.group.add(garc(LEFT * OFFSET, LEFT * OFFSET + WIDTH, 1))

    def calculate(self, in1, in2):
        return (in1 and not in2) or (not in1 and in2)

def garc(point1, point2, d):
    """
    General Arc:
    Draws an arc between two points where d is the distance from the circle's center to the chord
    """

    def flip_vector(point):
        flip = point.copy()
        flip[0] = point[1]
        flip[1] = -point[0]
        return flip

    sign = math.copysign(1, d)
    c = math.dist(point1, point2)
    r = math.hypot(c/2, d)
    theta = 2 * math.asin((c / 2) / r) * sign

    center = (point2 - point1) / 2
    norm = math.dist(center, [0,0,0])
    center = point1 + center + flip_vector(center) / norm * d

    sangle = math.atan2(point1[1] - center[1], point1[0] - center[0])

    return Arc(radius=r, start_angle=sangle, angle=-theta).shift(center)

def horizontal_zline(point1, point2):
    OFFSET = 0.02
    zag = (point2[0] - point1[0]) / 2
    zline = VGroup()
    zline.add(Line(start=point1, end=point1 + RIGHT * (zag + OFFSET)))
    zline.add(Line(start=point1 + RIGHT * zag, end=point2 + LEFT * zag))
    zline.add(Line(start=point2 + LEFT * (zag + OFFSET), end=point2))

    return zline

class BooleanExamples(Scene):
    def construct(self):
        bg = ImageMobject("..\\..\\..\\assets\\manim_bg.png")
        self.add(bg)

        title_group = self.title("Boolean Examples")
        mid_line = self.midline()
        title_group.add(self.list_examples())

        self.play(Unwrite(title_group), Uncreate(mid_line), lag_ratio=0)

        self.wait()

    def title(self, text):
        title = Text(text, font="Oxygen", color=TITLE_COLOR)
        title.shift(UP * 3)
        underline = Underline(title)
        self.play(Write(title), Write(underline))
        
        return VGroup(title, underline)

    def midline(self):
        line = Line(start=UP, end=DOWN * 2)
        self.play(Create(line))

        return VGroup(line)

    def list_examples(self):
        examples = VGroup()
        def create_example(text, translation):
            text_mobject = Text(text, font="Oxygen").shift(translation)
            examples.add(text_mobject)
            self.play(Write(text_mobject))
        
        create_example("true", LEFT * 1.5 + UP * 0.5)
        create_example("false", RIGHT * 1.5 + UP * 0.5)
        create_example("1", LEFT * 1.5 + DOWN * 0.5)
        create_example("0", RIGHT * 1.5 + DOWN * 0.5)
        create_example("accept", LEFT * 1.5 + DOWN * 1.5)
        create_example("reject", RIGHT * 1.5 + DOWN * 1.5)

        return examples
